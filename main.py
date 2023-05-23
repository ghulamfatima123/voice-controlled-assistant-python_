
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# sapi5 is used in windows to detect or recived voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# two voices male and female by default 
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <12:
        speak("Good Morning Ghulam Fatima !")
    elif hour >= 12 and hour <18:
        speak("Good Evening Ghulam Fatima !")
    else:
        speak("Good Evening")
    

    speak("I am your servent zain tell me how may i help you")

def  takeCommand():
    #docs string
    '''
    funcation takes output from user mic and return string output 
    '''
    speak("should i open music")
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listninng....!")
        r.pause_threshold= 1    
        audio= r.listen(source)

    try:
        print("Recognizing...!")
        query =r.recognize_google(audio,language='en-in')
        # query return string output
        print(f"User Said {query}\n")
    

    except Exception as e:
        print(e)
        print("say that again")
        return "None"

    return query
if __name__ == "__main__":
    speak("hey Ghulam Fatima please come here") 
    wishMe()
    while True:

        queury= takeCommand().lower()
        if 'wikipedia' in queury:
            speak('Searching wikipedia...')
            queury= queury.replace('wikipedia','')
            result =wikipedia.summary(queury,sentences=1)
            speak("according to wikipedia")
            print(result)
            speak(result) 
        
        elif 'open youtube' in queury:
            webbrowser.open("youtube.com")

        elif 'open google' in queury:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in queury:
            webbrowser.open("stackoverflow.com")
            

        elif 'paly music' in queury:
            music = 'directory'
            sogs =os.listdir(music) #list all the files which are in music
            os.startfile(os.path.join(music,sogs[0]))