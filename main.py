from assistant.speech import get_input, speak
from assistant.commands import handle_command

def main():
    print("\n=== SyntechHub Personal Voice Assistant ===")
    print("Choose input mode: text or voice")
    mode = input("Mode [text/voice]: ").strip().lower()
    if mode not in {"text", "voice"}:
        mode = "text"

    print("\nAssistant: Hello! I am your personal voice assistant.")
    speak("Hello! I am your personal voice assistant.")
    print("Type or say 'help' to see commands. Type or say 'exit' to stop.")

    while True:
        command = get_input(mode)
        if not command:
            print("I couldn't understand that. Please try again.")
            continue

        response, should_exit = handle_command(command)
        print(f"Assistant: {response}")
        speak(response)
        if should_exit:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant closed safely.")
