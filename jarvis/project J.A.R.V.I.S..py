import pyttsx3
import datetime
import speech_recognition as sr
import os
import datetime
import webbrowser as wb
import wikipedia
wb.register('chrome', None)
speech=sr.Recognizer()
engine=pyttsx3.init('sapi5')

try:
    engine = pyttsx3.init('sapi5')
except ImportError:
    print('rdinf')
except RuntimeError:
    print('dtfi')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
d=0
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio,chr(d))
    print("")

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good morning sir.")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir.")
    elif hour>=18 and hour<=23:
        speak("good evening sir.")
    elif hour>=0 and hour<6:
        speak("good night sir")
    return()
def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.........")
        r.pause_threshold=0.5
        audio=r.listen(source, timeout=0, phrase_time_limit=5)
    try:
        print("")
        query=r.recognize_google(audio,language='en-in')
        print("-->", query)
    except Exception as e:
        speak('')
        return(takecmd())      
    return(query)
    
    q=input("~~")
    return(q)

#if __name__ == "__main__":
def main():
    global d
    qb='no'
    speak("Hello")
    while True:
        if qb=='s':
            break
        else:
            pa=takecmd().lower()
            #assistant=pa[-1]
            if 'friday' in pa:
                voices = engine.getProperty('voices')
                engine.setProperty('voice',voices[1].id)
                d=3
                speak(' Hello Everyone. I AM '+ 'Friday' +'.')
            else:
                voices = engine.getProperty('voices')
                engine.setProperty('voice',voices[0].id)
                d=2    
                speak(' Hello Everyone. I AM '+ 'JARVIS' +'.')
            wishme()
            while True:
                query=takecmd().lower()
                if 'search about' in query:
                    speak("searching .....")
                    query=query.replace("search about","")
                    print(query)
                    try:
                        results=wikipedia.summary(query)
                        #print(query)
                        results=wikipedia.summary(query,sentences=5)
                        speak("according to wikipedia")
                        speak(results)
                    except Exception:
                        speak("Sorry Sir. No datas about your query "+chr(19))
                    
                    #print(results)
                    continue
                elif 'hotstar' in query:
                    wb.open('https://www.hotstar.com')
                    speak('Opening Hotstar')
                    continue
                elif 'skillrack' in query:
                    wb.open('https://skillrack.com')
                    speak('Opening Skillrack')
                elif 'open class' in query:
                    speak('Opening google classroom')
                    wb.open('https://classroom.google.com/u/0/h')
                    continue
                elif 'open youtube' in query:
                    speak('Opening Youtube')
                    wb.open("https://www.youtube.com/")
                    continue
                elif 'open google' in query:
                    wb.open("https://google.com/")
                    speak('Opening Google')
                    continue
                elif 'play some music' in query:
                    Music="C:\\Users\\91988\\Music\\Playlists\\Ed Sheeran - Shape of You [Official Video].mp3"
                    os.startfile(Music)
                    if 'next song' in query:
                        Music="C:\\Users\\91988\\Music\\Playlists\\Alan Walker - Faded(MP3_160K).mp3"
                        os.startfile(Music)
                        continue
                    elif 'play tamil music' in query:
                        Music="C:\\Users\\91988\\Music\\Playlists\\Kannaana Kanney Song with Lyrics _ Viswasam Songs(MP3_160K).mp3"
                        os.startfile(Music)
                        continue
                    elif 'stop music' in query:
                        os.stopfile(Music)
                        continue
                    continue
                elif 'open hackerrank' in query:
                    wb.open("https://www.hackerrank.com/dashboard")
                    continue
                elif 'open spotify' in query:
                    wb.open("https://open.spotify.com/playlist/37i9dQZF1E36lIBvK2pQjS")
                    continue                    
                elif 'time' in query:
                    time=datetime.datetime.now().strftime("%I:%M")
                    speak(time)
                    continue
                elif 'date' in query:
                    day=datetime.datetime.now().strftime("%D")
                    speak(day)
                    continue

                elif 'bye' in query:
                    speak('Hope you have enjoyed the session with my assistance')
                    speak('Incase i could not help surely i will improve myself to serve better in future')
                    speak('Thank you ')
                    qb='s'
                    break
                elif 'sleep' in query:
                    speak('OK SIR')
                    break
                else:
                    speak('command not yet learned')

                
                
if __name__ == "__main__":
    #print(wikipedia.summary('Pokemon', sentences=3))
    main()
