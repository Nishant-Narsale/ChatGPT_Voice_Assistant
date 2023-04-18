import speech_recognition as sr
# from chatgpt import command
from chatsonic import command
from speaker import speak

# creating a new instance of the SpeechRecognition class
r = sr.Recognizer()

# use the default microphone as the source for audio input
with sr.Microphone() as source:
    print("Say something! You have 10 seconds")
    # listen for audio and store it in memory
    audio = r.listen(source, 10, 10)
    print("Done listening")

# recognize speech using Google Speech Recognition
try:
    # convert speech to text
    text = r.recognize_google(audio)
    print("You said: {}".format(text))

    # send command to chatgpt
    res = command(text)
    print(res)

    #speaking text
    speak(res)

except sr.UnknownValueError:
    # handle unrecognized speech
    print("Sorry, I didn't understand that.")
except sr.RequestError as e:
    # handle API request errors
    print("Sorry, could not request results from Google Speech Recognition service; {0}".format(e))
