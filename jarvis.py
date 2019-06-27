import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0<= hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour < 6:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello I am Jarvis sir . How may I help you???")


def takecommand():
    """
    it takes microphone input and return string input . this function
    will take all our commands
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User Said: {query}\n")

    except sr.RequestError as e:
        error = "your network doesn't seem to be good or you are not connected"
        speak(error)
        print(error)
        return "None"
    except sr.UnknownValueError as e:
        print("Say that again please...")
        return "None"

    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('praveenjha8285@gmail.com','8285@jha')
    server.sendmail('praveenjha802@gmail.com',to,content)
    server.close()







if __name__ == "__main__":
    wishme()
    chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    while True:
        query = takecommand().lower()

        # logic how to use jarvis to do tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to My Knowledge')
            print(results)
            speak(results)

        elif 'bye' in query:
            speak('thank you , sir ')
            exit()

        elif 'quit' in query:
            speak('thank you , sir ')
            exit()

        elif 'open youtube' in query:
            webbrowser.get('chrome').open_new_tab('youtube.com')

        elif 'open google' in query:
            # webbrowser.open('google.com')  to open in defult internte explorer
            webbrowser.get('chrome').open_new_tab('google.com')

        elif 'play music' in query:
            music_dir="C:\\Users\\Praveen\\Desktop\\PREVIOUS FILES\\praveen personal\\audio"
            songs = os.listdir(music_dir)
            print(songs)
            from random import randint
            x = randint(0, 30)
            os.startfile(os.path.join(music_dir,songs[x]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "email to me"  in query:

            try:
                speak('what should i say?')
                content=takecommand()
                print('Sending...')
                to ="praveenjha802@gmail.com"
                sendemail(to,content)
                speak('your email has been sent')
                print('your email has been sent')
            except Exception as e:
                print(e)
                speak("sorry , my friend your email couldn't be sent ")

        elif "open " in query:
            os.system("explorer C:\\{}".format(query.replace('open ','')))
            speak('Opening...')
            print("Opening...")
