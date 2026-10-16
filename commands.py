from datetime import datetime
from urllib.parse import quote_plus
import platform
import subprocess
import webbrowser


def handle_command(command):
    """Process user commands."""

    text = " ".join(command.lower().strip().split())

    if not text:
        return "Please enter a command.", False

    if text in ["exit", "quit", "stop", "goodbye"]:
        return "Goodbye! Have a great day.", True

    if text in ["hello", "hi", "hey", "hello assistant"]:
        return "Hello! How can I help you?", False

    if text in ["help", "commands", "what can you do"]:
        return (
            "Commands: hello, time, date, search <topic>, "
            "open Google, open YouTube, open GitHub, "
            "open LinkedIn, open calculator, exit.",
            False
        )

    if "time" in text:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The time is {current_time}.", False

    if "date" in text:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}.", False

    if text.startswith("search "):
        query = text[7:].strip()

        if not query:
            return "Please tell me what to search for.", False

        url = "https://www.google.com/search?q=" + quote_plus(query)
        webbrowser.open(url)

        return f"Searching the web for {query}.", False

    if text.startswith("open "):
        target = text[5:].strip()

        websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com"
        }

        if target in websites:
            webbrowser.open(websites[target])
            return f"Opening {target.title()}.", False

        if target in ["calculator", "calc"]:
            try:
                system = platform.system()

                if system == "Windows":
                    subprocess.Popen(["calc.exe"])

                elif system == "Darwin":
                    subprocess.Popen(["open", "-a", "Calculator"])

                else:
                    subprocess.Popen(["gnome-calculator"])

                return "Opening calculator.", False

            except Exception:
                return "Unable to open the calculator.", False

        return "Unsupported application. Type help for commands.", False

    return (
        "Sorry, I did not understand. Type help to see commands.",
        False
    )
