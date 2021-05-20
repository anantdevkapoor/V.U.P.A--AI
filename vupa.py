from itertools import takewhile
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
import psutil 
import pyjokes
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time
import pyttsx3.drivers
hiddenimports = [
    'pyttsx3.drivers',
    'pyttsx3.drivers.dummy',
    'pyttsx3.drivers.espeak',
    'pyttsx3.drivers.nsss',
    'pyttsx3.drivers.sapi5', ]

wolframalpha_app_id='K49VGE-KTH9E9634A'
engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") 
    speak ("The Current Time is ")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak(" and the date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    speak("Welcome Back Sir")

def start():

    
    
   
    hour=datetime.datetime.now().hour
    if hour>=4 and hour<12:
       speak("Good Morning, Mr. Anant Dev Kapoor")
    elif hour>=12 and hour<15:
        speak("Good Afternoon, Mr. Anant Dev Kapoor")
    elif hour>=15 and hour<23:
        speak("Good Evening, Mr. Anant Dev Kapoor")
    else :
        speak("Good Night , Mr. Anant Dev Kapoor")
 
def sendemail(to,content):
   server=smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.login('email@gmail.com','password')
   server.sendmail('email@gmail.com',to,content)
   server.close()

def CPU():
    usage=str(psutil.cpu_percent())
    battery=psutil.sensors_battery()
    speak("Battery Percent is ")
    speak(battery.percent)
    speak("%")
    speak(" And CPU is at "+usage)
    speak("% Usage")

def Joke():
    speak(pyjokes.get_joke())

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:/Users/kapoo/OneDrive/Pictures/Screenshots/barry.png')

def TakeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone()  as source:
      print("V.U.P.A is listening.....")
      r.pause_threshold=.5
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
    
              
    try:
        print("V.U.P.A is recognizing....")
        query=r.recognize_google(audio,language='en-US')
      
        print(query)

    except Exception as ex:
        print(ex)
        print("Sorry I am not able to get you")
        return "None"
    return query 



if __name__=="__main__":
    start()
    greeting()
    ##CPU()
    while True:
     query =TakeCommand().lower()
     if 'time' in query:
         time_()

     elif 'date' in query:
         date_()
     elif 'wikipedia' in query:
         speak("Searching....")
         query=query.replace('wikipedia','')
         result=wikipedia.summary(query,sentences=3)
         speak('According to Wikipedia')
         print(result)
         speak(result)
     elif 'send mail' in query:
         try:
             speak("What Should I write?")
             content=TakeCommand()
             speak("Who is the reciever?")
             receiver=(input("Enter Email : "))
             to=receiver
             sendemail(to,content)
             speak("Email has been sent")
            
         except Exception as ex:
             print(ex)
             speak("Unable to send Email")
     elif 'open website' in query:
          speak("What Should I search?")
          chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
          search=TakeCommand().lower() 
          wb.get(chromepath).open_new_tab(search+'.com')  
     elif 'search youtube' in query:
         speak("What Should I look up?")
         search=TakeCommand().lower()
         speak("Opening Youtube Mr. Kapoor")
         wb.open('https://www.youtube.com/results?search_query='+search)
     elif 'search google' in query:
         speak("What should I search Mr. Kapoor")
         search=TakeCommand().lower()
         speak("Searching Sir.....")
         wb.open('https://google.com/search?q='+search)
     elif 'search instagram' in query:
         speak("What to Look up in INstagram Sir?")
         search=TakeCommand().lower()
         speak("Searching sir")
         wb.open('https://www.instagram.com/'+search)
     elif 'cpu usage'  in query:
         CPU()
     elif 'joke' in query:
         Joke()  
     elif 'exit' in query:
         speak("Have a good day Mr. Kapoor")
         quit()
     elif 'go offline' in query:
         speak("Going Offline Sir")
         quit()
     elif 'ms word' in query:
         speak("Opening MS Word....")
         msword=r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
         os.startfile(msword)
     elif 'ms powerpoint' in query:
         speak("Opening MS Powerpoint")
         mspoint=r'C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE'
         os.startfile(mspoint)
     elif 'ms excel' in query:
         speak("Opening MS Excel")
         msexcel=r'C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'
         os.startfile(msexcel)
     elif 'open chrome' in query:
         speak("Opening in Chrome")
         chrome=r'C:/Program Files/Google/Chrome/Application/Chrome.exe'
         os.startfile(chrome)
     elif 'write a note' in query:
         speak('What Should I write sir?')
         note=TakeCommand()
         file=open('note.txt','w')
         speak("Sir Should I include date and time")
         ans=TakeCommand()
         if 'yes' in ans or 'sure' in ans:
             Time=datetime.datetime.now().strftime("%H:%M:%S")
             file.write(Time)
             file.write(':-')
             file.write(note)
             speak("Done Taking notes Sir")
         else:
             file.write(note)
             speak("Done taking notes sir")
     elif 'show notes' in query:
            speak("Showing NOtes")
            file=open('note.txt','r')
            print(file.read())
            speak(file.read())
     elif 'take a screenshot' in query or 'take screensot' in query or 'screenshot' in query:
         screenshot()
     elif 'play songs' in query or 'play sound' in query:
         songsdir='C:/Users/kapoo/OneDrive/Desktop/Songs'
         speak("Which directory?")
         choice=TakeCommand().lower()
         if '1' in choice :
             songsdir='C:/Users/kapoo/OneDrive/Desktop/Songs/1'
             music=os.listdir(songsdir)
             speak('What Should I play?')
             ans=TakeCommand().lower()
             if 'number' in ans:
                 no=int(ans.replace('number',''))
             elif 'random' in ans or 'you choose' in ans:
                  no=random.randint(1,24)
                 
             os.startfile(os.path.join(songsdir,music[no]))

             
         elif '2'  in choice :
             songsdir='C:/Users/kapoo/OneDrive/Desktop/Songs/2'
             music=os.listdir(songsdir)
             speak('What Should I play?')
             ans=TakeCommand().lower()
             if 'number' in ans:
                 no=int(ans.replace('number',''))
             elif 'random' in ans or 'you choose' in ans:
                 no=random.randint(1,24)
             os.startfile(os.path.join(songsdir,music[no]))
         else:
             speak("Enter valid Input")
             print("Enter Valid Input")
        
     elif 'remember that' in query:
         speak("What Should I remember Sir?")
         memory=TakeCommand()
         speak("You asked me to remember"+memory)
         remember=open('memory.txt','w')
         remember.write(memory)
         remember.close()
     elif 'do you remember' in query:
         remember=open('memory.txt','r')
         speak('You asked me to remember '+remember.read())
     elif 'news' in query:
         try:
             newsp=urlopen("https://newsapi.org/v2/everything?q=tesla&from=2021-04-16&sortBy=publishedAt&apiKey=923ab0e93b0547a5a41137d8f3eda826")
             data=json.load(newsp)
             i=1
             speak("Here are some top lines from one month")
             print('=====================TOP HEADLINES===================='+'\n')
             for item in data['articles']:
                 print(str(i)+'. '+item['title']+'\n')
                 print(item['description']+'\n')
                 speak(item['title'])
                 i +=1
            
         except Exception as e:
                 print(str(e))

     elif 'where is' in query:
             query=query.replace("where is","")
             location=query
             speak("Mr. Kapoor you asked me to locate"+location)
             wb.open_new_tab("https://www.google.com/maps/place/"+location)
     elif 'calculate' in query:
         client=wolframalpha.Client(wolframalpha_app_id)
         indx=query.lower().split().index('calculate')
         res=client.query(''.join(query))
         answer=next(res.results).text
         print('The Answer is :'+answer)
         speak('The Answer is '+answer)
     elif 'what is' in query or 'who is' in query:
         client=wolframalpha.Client(wolframalpha_app_id)
         res=client.query(query)

         try:
             print(next(res.results).text)
             speak(next(res.results).text)
         except StopIteration:
             print("No Results")
     elif 'stop listening' in query:
         speak("For how many seconds do you want me to stop listening to your commands?")
         ans=int(TakeCommand())
         time.sleep(ans)
         print(ans)
     elif 'log out' in query:
         os.system("shutdown -1")
     elif 'restart' in query:
         os.system("shutdown /r /t 1")
     elif 'shutdown' in query:
         os.system("shutdown  /s /t 1")




            


