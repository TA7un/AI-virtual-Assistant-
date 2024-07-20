import pyttsx3
import os
import pyaudio
import webbrowser
import speech_recognition as sr
import tkinter as tk

class SampleApp(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.button = tk.Button(self, text="start", command=self.assistant)
		self.button.pack()
		self.entry = tk.Entry(self)
		self.entry.pack()
	def assistant(self):
		engine = pyttsx3.init()
		rate = engine.getProperty('rate')   # getting details of current speaking rate
		#print (rate)                        #printing current voice rate
		engine.setProperty('rate', 180)     # setting up new voice rate


		#"""VOLUME"""
		#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
		#print (volume)                          #printing current volume level
		#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
		voices = engine.getProperty('voices')
		engine.setProperty('voice', voices[1].id)
		pyttsx3.speak("I am your virtual assistant")
		pyttsx3.speak("\t\t\t How can i help you...?")
		while True:
			print("Tell me what can i do for you :" , end='')
			r = sr.Recognizer()
			with sr.Microphone() as source :
				print("start saying...")
				audio = r.listen(source)
				print("please wait...")
			p = r.recognize_google(audio)
			print(p)
			self.entry.insert(0,str(p))
			if (("run" in p) or ("execute" in p) or ("open" in p)) and (("Chrome" in p) or ("browser" in p)):
				pyttsx3.speak("opening your chrome browser please wait")
				os.system("start chrome")
			elif ("hello" in p) or ("hi" in p) or ("hey" in p):
				pyttsx3.speak("Hello sir i am Lisa \t your virtual assistant \t How can i help you...? ")
			elif (("show" in p) or ("open" in p)) and ("Date" in p):
				pyttsx3.speak("showing todays date")
				os.system("date")
			elif (("run" in p) or ("open" in p)) and (("Google cloud" in p) or ("GCP" in p)):
				pyttsx3.speak("opening google cloud")
				webbrowser.open("cloud.google.com")
			elif (("run" in p) or ("open" in p)) and (("aws" in p) or ("Cloud services" in p)):
				pyttsx3.speak("opening amazon web services")
				webbrowser.open("aws.amazon.com")
			elif (("run" in p) or ("open" in p)) and ("Flipkart" in p):
				pyttsx3.speak("opening flipkart")
				webbrowser.open("www.flipkart.com")
			elif (("show" in p) or ("open" in p)) and ("Time" in p):
				pyttsx3.speak("showing current time")
				os.system("time")
			elif (("run" in p) or ("open" in p)) and ("Spotify" in p):
				pyttsx3.speak("opening spotify")
				webbrowser.open("www.spotify.com")
			elif (("run" in p) or ("open" in p)) and ("Yahoomail" in p) or ("Yahoo mail" in p):
				pyttsx3.speak("opening yahoo mail")
				webbrowser.open("www.yahoomail.com")
			elif (("run" in p) or ("open" in p)) and ("Puttygen" in p):
				pyttsx3.speak("opening putty")
				os.system("start puttygen")
			elif (("run" in p) or ("open" in p)) and ("Putty" in p):
				pyttsx3.speak("opening putty")
				os.system("start putty")
			elif (("run" in p) or ("open" in p)) and (("Virtualbox" in p) or ("Virtual box" in p)):
				pyttsx3.speak("opening Vbox")
				os.system("start virtualbox")
			elif (("run" in p) or ("open" in p)) and ("Discord" in p):
				pyttsx3.speak("opening discord")
				os.system("start discord")
			elif (("can" in p) or ("you" in p)) and ("name" in p): 
				pyttsx3.speak("your name is Tarun Ghutey and you have a short temper personality")
			elif (("can" in p) or ("tell" in p)) and (("name" in p) or ("about" in p)): 
				pyttsx3.speak("your name is Tarun Ghutey and you are the person who created me ")
			elif (("run" in p) or ("open" in p)) and ("Slack" in p):
				pyttsx3.speak("opening slack")
				os.system("start slack")
			elif (("run" in p) or ("open" in p)) and ("Steam" in p):
				pyttsx3.speak("opening steam")
				os.system("start steam")
			elif (("run" in p) or ("open" in p)) and ("Anydesk" in p):
				pyttsx3.speak("opening anydesk")
				os.system("start anydesk")
			elif (("run" in p) or ("open" in p)) and ("TeamViewer" in p):
				pyttsx3.speak("opening team viewer")
				os.system("start TeamViewer")
			elif(("run" in p) or ("open" in p)) and ("Firefox" in p):
				os.system("start firefox")
			elif("Google" in p):
				webbrowser.open("www.google.com")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("WhatsApp" in p):
				webbrowser.open("https://web.whatsapp.com/")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("Instagram" in p) or ("insta" in p)):
				webbrowser.open("https://www.instagram.com/")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("Facebook" in p) or ("FB" in p)):
				webbrowser.open("https://www.facebook.com/")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("Youtube" in p):
				webbrowser.open("https://www.youtube.com/")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("Telegram" in p):
				webbrowser.open("https://web.telegram.org/#/im")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("mail" in p) or ("Gmail" in p) or ("Google mail" in p):
				webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("Twitter" in p):
				webbrowser.open("https://www.twitter.com/")
			elif (("Run" in p) or ("execute" in p) or ("open" in p)) and (("Notepad" in p) or ("notepad" in p)):
				os.system("start notepad")
			elif (("run" in p) or ("execute" in p)) and ("player" in p) and ("media" in p):
				os.system("start wmplayer")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("Paint" in p):
				os.system("start mspaint")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("WordPad" in p):
				os.system("start wordpad")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("KMPlayer" in p):
				os.system("start kmplayer")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("VLC" in p):
				os.system("start vlc")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("camera" in p):
				os.system("start microsoft.windows.camera:")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("calculator" in p):
				os.system("start calculator:")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("clock" in p):
				os.system("start ms-clock:")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("calendar" in p):
				os.system("start outlookcal:")
			elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("map" in p) or ("maps" in p)):
				os.system("start ms-walk-to:")
			elif ("exit" in p) or ("quit" in p) or ("stop" in p):
				pyttsx3.speak("see you soon,, have a nice day...!!!")
				break
			else:
				print("sorry this command is not availabe please try again")
				pyttsx3.speak("sorry sir this command is not availabe please try again")

app = SampleApp()
app.mainloop()
