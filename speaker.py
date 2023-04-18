import pyttsx3  

# initialize Text-to-speech engine  
engine = pyttsx3.init()  

# convert this text to speech  
def speak(text):
    engine.say(text)  
    # play the speech  
    engine.runAndWait() 

if __name__ == "__main__":
    speak("Hi sir, How are you?")