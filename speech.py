def speak(text):
    """Convert text into speech."""
    try:
        import pyttsx3

        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception:
        print("Voice output is unavailable.")


def get_input(mode):
    """Get commands from voice or keyboard."""

    if mode != "voice":
        return input("\nYou: ").strip()

    try:
        import speech_recognition as sr

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(
                source, duration=0.4
            )
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You:", command)
        return command

    except Exception as error:
        print("Voice input unavailable:", error)
        return input("\nYou: ").strip()
