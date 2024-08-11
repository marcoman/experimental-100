import PyPDF2

# One TTS library
import pyttsx3

# The Google TTS library
from gtts import gTTS
import pygame

import os
import requests
import json
import base64

def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            print (f'reading page {page_num}')
            text += pdf_reader.pages[page_num].extract_text()
    return text

def display_text(text):
    print('The text in your document is: ')
    for line in text.splitlines():
        print(line)

def text_to_speech_pttsx3(text):
    tts_engine = pyttsx3.init()

    for line in text.splitlines():
        print(line)
        tts_engine.say(line)
        tts_engine.runAndWait()

def text_to_speech_gtts(text):
    print("Playing gTTS")
    language = 'en'
    myTTS = gTTS(text=text, lang=language, slow=False)
    print("Saving output file as output.mp3")
    myTTS.save("output.mp3")
    pygame.mixer.init()
    print("loading output.mp3")
    pygame.mixer.music.load("output.mp3")
    print("playing output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print("done playing")
    pygame.mixer.quit()

def text_to_speech_google(text):
    # This is the API key for the Google Cloud Text-to-Speech service
    api_key = os.environ.get('gcloud_api_key')
    project_id = os.environ.get('PROJECT_ID')
    print (f'api key is {api_key}')
    print (f'project id is {project_id}')

    # The URL for the Google Cloud Text-to-Speech API
    url = f'https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}'

    # The headers for the API request
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
    }

    # The data for the API request
    data = {
        'input': {
            'text': text
        },
        'voice': {
            'languageCode': 'en-US',
            'name': 'en-US-Standard-C',
            'ssmlGender':'FEMALE'

        },
        'audioConfig': {
            'audioEncoding': 'MP3'
        }
    }

    # Send the API request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        # Save the audio file
        response_data = response.json()
        audio = response_data['audioContent']
        audio_binary = base64.b64decode(audio)
        with open('google.mp3', 'wb') as f:
            f.write(audio_binary)
        print('Audio file saved as google.mp3')
    else:
        print('Error:', response.text)

# This sequence works.
mytext = extract_text_from_pdf('sample-text.pdf')
display_text(mytext)

# now we have to do text-to-speech with a python library.
# text_to_speech_gtts(mytext)

# This call works to a more basic python library.
# text_to_speech_pttsx3(mytext)

# Now let's invoke an API call and get the results.   I'll use this as a my inspiration:
# https://cloud.google.com/text-to-speech/docs/basics

# I'll need an authorization token from google cloud.
text_to_speech_google(mytext)
