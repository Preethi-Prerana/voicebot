## for speech-to-text
import speech_recognition as sr

## for text-to-speech
from gtts import gTTS

## for language model
import transformers

## for data
import os
import datetime
import numpy as np

from prediction import predictDisease
from extractor import extract_symptoms
sym=""

# Build the AI
class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")

    @staticmethod
    def text_to_speech(text):
        print("ai --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)

    def wake_up(self, text):
        return True if self.name in text.lower() else False


# Run the AI
if __name__ == "__main__":
    
    ai = ChatBot(name="maya")
    start=True

    while start:
        ai.speech_to_text()

        ## wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am MAYA the med-bot, what can I do for you?"
        
        ## action diagnosis
        elif "diagnosis" in ai.text:
            ai.text_to_speech("Ohh that's sad...")
            ai.text_to_speech('Could you please list the symptoms...')
            ai.speech_to_text()
            while "nothing" not in ai.text:
                if(len(ai.text)!=0)
                    sym=sym+extract_symptoms(ai.text)+","
                ai.text_to_speech('Do you experience any more symptoms...')
                ai.speech_to_text()
            ai.text_to_speech('Please wait for a minute....')
            res = predictDisease(sym[:-1].title())['final_prediction']
        
        ## respond politely
        elif any(i in ai.text for i in ["thank","thanks"]):
            res = np.random.choice(["you're welcome! I'm here if you need me!"])
            start=False
        
        ## conversation
        else:   
            res="Sorry....Could you please repeat...."

        ai.text_to_speech(res)