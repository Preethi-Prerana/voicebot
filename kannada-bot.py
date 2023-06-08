# -- coding: utf-8 --
import speech_recognition as sr
import nltk
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from gtts import gTTS
from playsound import playsound
# from IPython.display import Audio

# Define the symptoms and diseases CSV file path
CSV_FILE_PATH = "symptoms.csv"

# Load the symptoms and diseases data into a pandas DataFrame
df = pd.read_csv(CSV_FILE_PATH)

# Extract the symptoms as text and the diseases as labels
symptoms = df['Symptoms'].values
diseases = df['Diseases'].values

# Convert the symptoms into a sparse matrix of TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(symptoms)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, diseases, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Set up the speech recognition engine
r = sr.Recognizer()

# Define a function to recognize speech and return the text


def recognize_speech():
    with sr.Microphone() as source:
        print("\n\tನಮಸ್ಕಾರ ನಾನು ನಿಮ್ಮ ಸಹಾಯಕ ದಿ ಮೆಡ್-ಬೊಟ್")
        print("ನಿಮ್ಮ ಲಕ್ಷಣಗಳನ್ನು ಹೇಳಿರಿ...\n")
        print("Speak now...")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="kn-IN")
        return text

# Define a function to predict the disease based on symptoms


def predict_disease(symptoms):
    # Convert the symptoms into a sparse matrix of TF-IDF features
    X = vectorizer.transform([symptoms])
    # Predict the disease label using the trained classifier
    y_pred = clf.predict(X)
    return y_pred[0]

# Define a function to convert text to speech in Kannada


def text_to_speech_kn(text):
    # Initialize a gTTS object with the text and language
    speech = gTTS(text=text, lang='kn')
    # Save the speech as an mp3 file
    speech.save("output.mp3")

    # Audio('output.mp3', autoplay=True)
    # Play the mp3 file using the playsound library
    os.system("start output.mp3")


start = True
# Start the main loop for the voice-bot
while start:
    # Get the user's symptoms from speech input
    symptoms = recognize_speech()
    print(f"You said: {symptoms}")

    # Predict the disease based on the symptoms
    disease = predict_disease(symptoms)
    print(f"Predicted disease: {disease}")

    # Convert the predicted disease into Kannada speech output
    output_text = f"ನೀವು ಹೇಳಿದ ಲಕ್ಷಣಗಳಿಂದ ನಿಮ್ಮ ರೋಗ {disease} ಆಗಿರಬಹುದು"
    text_to_speech_kn(output_text)

    start = False
