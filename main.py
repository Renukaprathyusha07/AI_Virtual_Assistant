from voice import speak, take_voice_command, take_text_command
from assistant import process_command


def main():

    speak("Welcome to AI Virtual Assistant")

    while True:

        print("\n========== AI VIRTUAL ASSISTANT ==========")
        print("1. Voice Command")
        print("2. Text Command")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            command = take_voice_command()

            if process_command(command) is False:
                break

        elif choice == "2":

            command = take_text_command()

            if process_command(command) is False:
                break

        elif choice == "3":

            speak("Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()