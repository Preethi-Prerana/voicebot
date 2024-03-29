# for speech-to-text
from extractor import extract_symptoms
from prediction import predictDisease
from prelim_medication import prelim_medi
# import numpy as np
import speech_recognition as sr

# for text-to-speech
from gtts import gTTS

from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak


sym = ""

# Build the AI


class ChatBot():
    def __init__(self, name):
        print("--- starting up", name, "---")
        speak("starting up doctor")
        self.name = name

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ",self.text)
        except:
            print("me -->  ERROR")
            speak("error")

    @staticmethod
    def text_to_speech(text):
        print("ai --> ",text)
        speak(text)
        speaker = gTTS(text=text )#, lang="kn", slow=False)

    def wake_up(self, text):
        return True if self.name in text.lower() else False


# Run the AI
if __name__ == "__main__":
    ai = ChatBot(name="doctor")
    start = True

    while start:
        ai.speech_to_text()

        # wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Doctor the med-bot, what can I do for you?"

        # action diagnosis
        elif "diagnosis" in ai.text:
            ai.text_to_speech('Could you please list the symptoms...')
            ai.speech_to_text()
            while "nothing" not in ai.text:
                if len(ai.text) != 0:
                    sym = sym+extract_symptoms(ai.text)+","
                ai.text_to_speech('Do you experience any more symptoms...')
                ai.speech_to_text()
            ai.text_to_speech('Please wait for a minute....')
            s1 = "You might be suffering from "
            s2 = "\nPreliminary medications are "
            disease = predictDisease(sym[:-1].title())['final_prediction']
            medication = prelim_medi(disease)
            res = s1 + disease +s2+medication


        # respond politely
        elif any(i in ai.text for i in ["thank", "thanks"]):
            # ai.text_to_speech("Would you like to have any further assistance")
            res = "Thank you!!I am here if you need me.."
            start = False

        # conversation
        else:
            res = "Sorry....Could you please repeat...."
        ai.text_to_speech(res)
        
#end
