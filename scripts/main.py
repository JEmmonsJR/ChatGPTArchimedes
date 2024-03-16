import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """
    Function to speak the given text.
    """
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Function to listen for audio and return the recognized text.
    """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def archimedes():
    """
    Main function for Archimedes voice assistant.
    """
    speak("Hello, I am Archimedes. How can I assist you today?")
    
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "how are you" in query:
            speak("I'm doing well, thank you for asking!")
        elif "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you repeat?")
    
if __name__ == "__main__":
    archimedes()
