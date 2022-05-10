import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        speak("Good Morining")
    
    elif hours>=12 and hours<18:
        speak("Good Afternoon")

    else:
        speak("Good eveninhg")

    speak("I am jarvis sir. Please tell me how may I help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:, {query}\n" )

    except Exception as e:
        # print(e)

        print("Say that again please.....")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'shutdown' in query:
            speak("do you really want to shutdown the system sir")
            replay = takeCommand().lower()
            if 'yes' in replay:
                os.system('Shutdown /s /t 1')
            else:
                
                speak("As you wish, sir")

        
        elif 'restart' in query:
            speak("do you really want to restart the system sir")
            replay = takeCommand().lower()
            if 'yes' in replay:
                os.system('Shutdown /r /t 1')
            else:
                speak("As you wish, sir")