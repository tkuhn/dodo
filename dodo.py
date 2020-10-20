import speech_recognition as sr
import os

normal = "\n"*7+" "*37+"~   ~\n"+" "*37+"o   o\n"+" "*39+"'\n"+" "*37+" ___ "+"\n"*8
smile = "\n"*7+" "*37+"~   ~\n"+" "*37+"o   o\n"+" "*39+"'\n"+" "*37+"\___/"+"\n"*8
speaking = "\n"*7+" "*37+"~   ~\n"+" "*37+"o   o\n"+" "*39+"'\n"+" "*37+"  O  "+"\n"*8
confused = "\n"*6+" "*37+"  ?\n"+" "*37+"~   ~\n"+" "*37+"o   o\n"+" "*39+"'\n"+" "*37+"  _  "+"\n"*8
gone = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

next = normal

r = sr.Recognizer()
while True:
  with sr.Microphone(sample_rate=8000) as source:
    os.system("clear")
    print(next)
    audio = r.record(source, 2)
    try:
      text = r.recognize_sphinx(audio,
        keyword_entries=[('dodo',1.0),('ciao',1.0),('bravo',1.0),('charlie',1.0)])
      text = " " + text;
      if (text == " dodo  ciao "):
        os.system("clear")
        print(speaking)
        os.system("espeak -v+f5 'ciao ciao'")
        os.system("clear")
        print(gone)
        break
      elif (" dodo " in text):
        os.system("clear")
        print(speaking)
        next = smile
        os.system("espeak -v+f5 'dodo'")
      else:
        next = confused
        #os.system("espeak -v+f5 '{}'".format(text))
    except:
        next = normal
