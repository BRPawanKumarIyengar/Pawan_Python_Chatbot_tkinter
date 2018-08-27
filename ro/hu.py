from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import os
import win32com.client as Bolna


Vaachal = Bolna.Dispatch('SAPI.SpVoice')

Batuni = ChatBot('Test')
Batuni.set_trainer(ListTrainer)

for Text_Files in os.listdir('yo'):
	Baat_Cheet = open('yo/' + Text_Files,'r').readlines()
	Batuni.train(Baat_Cheet)


#Vaachal.Speak('Hello! I am Batuni .... the chatbot. I would love to chat with you')

def Bolte_Raho(SunLo):
	while True:
		request = SunLo
		if request == 'bye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
		
		if request == 'Bye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
		
		if request == 'Exit':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'exit':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
		
		if request == 'terminate':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
		
		if request == 'terminate':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'GoodBye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'goodbye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			break
	
		if request == 'Good Bye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'good bye':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'Stop Chat':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		if request == 'stop chat':
			Vaachal.Speak('chat shall now terminate ... GoodBye!')
			Vaapis = 'Batuni:  ' + 'chat shall now terminate ... GoodBye!'
			return Vaapis
			break
	
		response = Batuni.get_response(request)
		Vaachal.Speak(response)
		Vaapis = 'Batuni:  ' + response.text
		return Vaapis