import pyttsx3
import openai
import speech_recognition as sr
# Set up OpenAI API credentials
openai.api_key = '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'

# Set up speech recognition
recognizer = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()


def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("User: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, an error occurred.")
        return ""


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()


conversation = ""
text_to_speech("Hello, how can I assist you today?")

while True:
    # Speech input from the user
    user_input = speech_to_text()
    if user_input:
        conversation += 'User: ' + user_input + '\n'

        # Get response from the chatbot
        response = chat_with_gpt(conversation)
        print("Chatbot:", response)
        text_to_speech(response)

        conversation += 'Chatbot: ' + response + '\n'


'''import speech_recognition as sr
import pyttsx3
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Set up speech recognition
recognizer = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()

def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("User: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, an error occurred.")
        return ""

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()

conversation = ""
text_to_speech("Hello, how can I assist you today?")

while True:
    # Speech input from the user
    user_input = speech_to_text()
    if user_input:
        conversation += 'User: ' + user_input + '\n'

        # Get response from the chatbot
        response = chat_with_gpt(conversation)
        print("Chatbot:", response)
        text_to_speech(response)

        conversation += 'Chatbot: ' + response + '\n'
'''
