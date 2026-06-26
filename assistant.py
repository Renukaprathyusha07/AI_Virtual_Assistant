from voice import speak
import commands


def process_command(command):
    """
    Process the user's command and execute the appropriate function.
    """

    if not command:
        return

    # Time
    if "time" in command:
        response = commands.get_time()
        speak(response)

    # Date
    elif "date" in command:
        response = commands.get_date()
        speak(response)

    # Google
    elif "open google" in command:
        response = commands.open_google()
        speak(response)

    # YouTube
    elif "open youtube" in command:
        response = commands.open_youtube()
        speak(response)

    # Notepad
    elif "open notepad" in command:
        response = commands.open_notepad()
        speak(response)

    # Calculator
    elif "open calculator" in command:
        response = commands.open_calculator()
        speak(response)

    # Wikipedia Search
    elif "wikipedia" in command:
        speak("What do you want to search?")
        query = input("Wikipedia Search: ")
        response = commands.search_wikipedia(query)
        speak(response)

    # Google Search
    elif "search" in command:
        query = command.replace("search", "").strip()

        if query == "":
            query = input("Google Search: ")

        response = commands.google_search(query)
        speak(response)


    # Play Music
    elif "play music" in command:
        response = commands.play_music()
        speak(response)

    # Exit
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I don't know that command yet.")

    return True