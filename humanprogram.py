import pyttsx3
import os
pyttsx3.speak("Hello sir how can i help you")
while True:
	print("Tell me what can i do for you :" , end='')
	p=input()
	if (("run" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
		os.system("start chrome")
	elif(("run" in p) or ("execute" in p)) and ("firefox" in p):
		os.system("start firefox")
	elif("google" in p):
		os.system("start firefox www.google.com")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("whatsapp" in p):
		os.system("start firefox https://web.whatsapp.com/")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("instagram" in p) or ("insta" in p)):
		os.system("start firefox https://www.instagram.com/")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("facebook" in p) or ("fb" in p)):
		os.system("start firefox https://www.facebook.com/")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("youtube" in p):
		os.system("start firefox https://www.youtube.com/")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("telegram" in p):
		os.system("start firefox https://web.telegram.org/#/im")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("mail" in p) or ("gmail" in p) or ("google mail" in p):
		os.system("start firefox https://mail.google.com/mail/u/0/#inbox")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("twitter" in p):
		os.system("start firefox https://www.twitter.com/")
	elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
		os.system("start notepad")
	elif (("run" in p) or ("execute" in p)) and ("player" in p) and ("media" in p):
		os.system("start wmplayer")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("paint" in p):
		os.system("start mspaint")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("wordpad" in p):
		os.system("start wordpad")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("kmplayer" in p):
		os.system("start kmplayer")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("vlc" in p):
		os.system("start vlc")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("camera" in p):
		os.system("start microsoft.windows.camera:")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("calculator" in p):
		os.system("start calculator:")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("clock" in p):
		os.system("start ms-clock:")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("calendar" in p):
		os.system("start outlookcal:")
	elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("maps" in p):
		os.system("start ms-walk-to:")
	elif ("exit" in p) or ("quit" in p) or ("stop" in p):
		break
	else:
		print("sorry sir this command is not availabe please try again")
		pyttsx3.speak("sorry sir this command is not availabe please try again")