# Overview

This is the day 91 assignment.

## _From the course:_
Write a Python script that takes a PDF file and converts it into speech.

Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech. Effectively creating a free audiobook.

AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.

Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.

You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:

http://www.ispeech.org/api/#introduction

https://cloud.google.com/text-to-speech/docs/basics

https://aws.amazon.com/polly/



## My comments:

This looks to be a fun application.  I'll write up a sample word document and then export it to a PDF.
I expect to find a library to read the contents of a PDF, specfically the body.
I also expect to find a Python library that can to TTS (Text to Speech).
I'll make the application fairly simple, it reads a hard-coded file name and announcing the words.


First the PDF.  I searched and found libraries such as pyPdf, PyPDF2, and PyPDF4.  I'll start with pypdf2.



# Running

To test the curl invocation, run a command like the following, assuming you have a gcloud account and set an environment variable with your `PROJECT_ID`:


```bash
curl -H "Authorization: Bearer "$(gcloud auth print-access-token) -H "x-goog-user-project: ${PROJECT_ID}" -H "Content-Type: application/json; charset=utf-8" --data "{
  'input':{
    'text':'Your attention please.  Testing 1 2 3'
  },
  'voice':{
    'languageCode':'en-gb',
    'name':'en-GB-Standard-A',
    'ssmlGender':'FEMALE'
  },
  'audioConfig':{
    'audioEncoding':'MP3'
  }
}" "https://texttospeech.googleapis.com/v1/text:synthesize" > response.mp3
```

```bash
python3 pdf-to-speech.py
```

# External Links

- [Google TTS API](https://cloud.google.com/sdk/docs/install#deb)
- [Google documentation](https://cloud.google.com/text-to-speech/docs/basics)


# requirements.txt


```shell\
sudo apt install espeak
sudo apt install alsa
sudo apt-get install apt-transport-https ca-certificates gnupg curl
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-cli

pip install pypdf2
pip install pyttsx3
pip install gTTS
pip install pygame
```


# TODOs

