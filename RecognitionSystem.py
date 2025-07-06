import speech_recognition as sr
import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Recognizer Initialization
recognizer = sr.Recognizer()

# Predefined Commands and Actions
commands = {
    "open notepad": "notepad.exe",
    "open calculator": "calc.exe",
    "open browser": "start chrome",
    "shutdown": "shutdown /s /t 1"
}

print("Say a command...")

# Main Loop
while True:
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            # Check if command matches predefined
            if command in commands:
                speak(f"Executing {command}")
                os.system(commands[command])
            elif "exit" in command or "quit" in command:
                speak("Exiting. Goodbye!")
                break
            else:
                speak("Sorry, command not recognized.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError:
        print("Check your internet connection.")
