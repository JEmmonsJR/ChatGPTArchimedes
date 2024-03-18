import speech_recognition as sr
import pyttsx3
import json
import requests
import webbrowser

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load API key from JSON file
with open("D:\Code Projects\ChatGPTArchimedes\key\keys.json") as fi:
    credentials = json.load(fi)

WEATHER_KEY = credentials['weather_key']


def speak(text):
    """
    Function to speak the given text.
    """
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    """
    Function to open YouTube in the default web browser.
    """
    webbrowser.open("https://www.youtube.com")

def listen():
    """
    Function to listen for audio and return the recognized text.
    """
    with sr.Microphone(device_index=1) as source:
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

def get_weather(city):
    """
    Function to fetch weather information for a given city.
    """
    api_key = WEATHER_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather_desc = data['weather'][0]['description']
        temperature = data['main']['temp']
        temperature_celsius = temperature - 273.15  # Convert temperature to Celsius
        return f"The weather in {city} is {weather_desc} with a temperature of {temperature_celsius:.2f}°C."
    else:
        return "Sorry, I couldn't fetch the weather information for that city." 

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
        elif "weather" in query:
            city = query.split("weather in ")[-1].capitalize()
            response = get_weather(city)
            speak(response)
        elif "open youtube" in query:
            speak("Opening YouTube.")
            open_youtube()
        elif "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Can you repeat?")
    
if __name__ == "__main__":
    archimedes()
