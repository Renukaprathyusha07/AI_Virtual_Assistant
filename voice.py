import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)


def speak(text):
    """Convert text to speech."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def take_voice_command():
    """Listen to the microphone and return the user's voice command."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)

            print("You:", command)
            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand you.")
            return ""

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""


def take_text_command():
    """Accept text input from the keyboard."""
    command = input("\nType your command: ")
    return command.lower()