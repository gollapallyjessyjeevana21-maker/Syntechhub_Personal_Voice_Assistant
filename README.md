# SyntechHub Personal Voice Assistant

## Project overview
This Python project is a personal voice assistant that accepts voice or typed commands and responds with text and optional speech.

## Features
- Speech-to-text input using SpeechRecognition.
- Text-to-speech responses using pyttsx3.
- Rule-based command mapping.
- Tells the current time and date.
- Opens Google, YouTube, GitHub, and LinkedIn.
- Searches the web for a user-provided topic.
- Attempts to open the computer's calculator.
- Handles unsupported commands and unavailable audio devices.

## Technologies
- Python 3.10+
- SpeechRecognition
- pyttsx3
- Python `webbrowser`, `datetime`, and `subprocess` modules

## Project structure
```text
Syntechhub_Personal_Voice_Assistant/
├── main.py
├── requirements.txt
├── README.md
└── assistant/
    ├── __init__.py
    ├── speech.py
    └── commands.py
```

## Installation
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python main.py
   ```

## How to use
Choose `text` or `voice` mode when the program starts.

Example commands:
- `hello`
- `what time is it`
- `what is today's date`
- `search Python tutorials`
- `open YouTube`
- `open GitHub`
- `open calculator`
- `help`
- `exit`

## Notes and limitations
- Voice recognition may require an internet connection and microphone access.
- Microphone support can require additional operating-system audio dependencies.
- If voice input is unavailable, choose text mode.
- Calculator launching depends on the operating system and installed desktop environment.
- This is an educational internship project, not a production-grade assistant.
