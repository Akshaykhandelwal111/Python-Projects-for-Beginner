import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import spotify
import webbrowser
import wkikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def wishme():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("good morning")
  elif hour>=12 and hour<18:
    speak("good aftermoon")
  else:
    speak("good evening")
    speak("i am jarvis .please tell me how may i help you")
def takecommand():
  """it take microphone input"""
  r=sr.Recongnizer()
  with sr.Microphone() as source:
    print("listing")
    r.pause_threshold =1
    audio= r.listen(source)
  try:
    print("recoginizing", r.recognize_google(audio))
    query= r.recognize_google(audio, langauge='en-in')
    print(f"user said:{query}\n")
    
  except Exception as e:
    print("say that again please...")
    return "none"
  return query
# except :
# print("unable to reconige the audio")
# query =.recognize_google(audio, language='en-in')
#print(f"user said:{query}]n")

if __name__== '__main__': 
  speak("hlo tony how are you")
  wishme()
  while True:
    query=takecommend(). lower()
    """if 'open youtube' in query:
    webbrowser.open ("youtube.com")"""
    
    if 'wikipedia' in query:
      speak("searching wikipedia")
      query=query.replace("wikipedia","")
      results=wikipedia.summary(query,sentences=2)
      speak("according to wikipedia")
      print(results)
      speak(results)
    elif 'open youtube' in query:
      webbrowser.open("youtube.com")
    elif 'open spotify' in query:
      webbrowser.open("spotify.com")
    elif 'open google' in query:
      webbrowser.open("google.com")
    elif 'the time' in query:
      strtime=datetime.datetime.now("%HH:%MM:%SS")
      speak(f"mam, time is {strtime}")
    elif 'jarvis' in query:
      speak("yes tony")
      print("yes tony")
  
    
      
    
 
