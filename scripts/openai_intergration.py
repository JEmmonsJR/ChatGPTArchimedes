import openai
import json
from openai import OpenAI

# Load API key from JSON file
with open("D:\Code Projects\ChatGPTArchimedes\key\keys.json") as fi:
    credentials = json.load(fi)

API_KEY = credentials['apikey']

# Set OpenAI API key
client = OpenAI(api_key=API_KEY)

# Define function to interact with Archimedes
def ask_archimedes(question):
    response = client.completions.create(model="text-davinci-002",  # Use "text-davinci-002" model
        prompt=question + "\nArchimedes:",
        temperature=0.7,
        max_tokens=150)
    return response.choices[0].text.strip()

# Main function for user interaction
def main():
    print("Welcome to Archimedes, your virtual assistant.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = ask_archimedes(user_input)
        print("Archimedes:", response)

if __name__ == "__main__":
    main()
