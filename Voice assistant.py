import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Request failed."


while True:
    print("Say something...")
    user_input = listen()
    print(f"You said: {user_input}")
    if "exit" in user_input.lower():
        speak("Goodbye!")
        break
    else:
        response = f"You said: {user_input}"
        speak(response)
