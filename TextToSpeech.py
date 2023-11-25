import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("voice", "")

print("Welcome to RoboSpeaker 1.1. Created by PersistantFate")

while True:
    text = input("Enter the text you want to convert to speech: ")

    if text == "q":
        print("Bye Bye")
        break

    engine.say(text)
    engine.runAndWait()
    
