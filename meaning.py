import messagebox
import requests
from bs4 import BeautifulSoup
#import speech_recognition as sr
#import sys
#from difflib import SequenceMatcher
def func(word):
 url="http://www.urbandictionary.com/define.php?term="
 url=url+word
 print(url)
 r=requests.get(url)
 b=BeautifulSoup(r.text)
 t=b.find('div',{"class":"meaning"})
 print(t.text)
 return t.text
if __name__=="__main__":
 #r = sr.Recognizer()
 #with sr.Microphone() as source:
  #print("Say something!")
  #audio = r.listen(source)
  #voice=r.recognize_google(audio)
  #text=func(voice)
  #messagebox.display(text)
 func('code')
 
 
