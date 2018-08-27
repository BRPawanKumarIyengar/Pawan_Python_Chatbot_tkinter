from tkinter import *
from tkinter import scrolledtext
import hu

window = Tk()
window.title("ChatBot Batuni")
lbl = Label(window, text= 'Batuni:  Hello! I am Batuni .... the chatbot. I would love to chat with you',bg = 'green',width=118,borderwidth = 0, highlightthickness = 0, fg='white')
lbl.grid(column=0, row=0,columnspan = 2)

lbl2= Label(window, text= 'Type Your Text here',height = 5,width=60,bg='gold')
lbl2.grid(column=0, row=2 )

Text_Wala_Box = Text(window, height=5, width=50, bg='red')	
Text_Wala_Box.grid(column=1, row=2)

Counter_Ganit = 0
Poori_Baat = 'Batuni:  Hello! I am Batuni .... the chatbot. I would love to chat with you'

ScrlBar = scrolledtext.ScrolledText(window,height =5)
ScrlBar.grid(column=0,row =1, columnspan=2)
ScrlBar.configure(width=102,bg='green',fg='cyan')

def clicked(): 
	input = Text_Wala_Box.get("1.0",'end-1c')
	if input != '':		
		Jawab = hu.Bolte_Raho(input)
		global Counter_Ganit
		global Poori_Baat
		Poori_Baat = Poori_Baat + '\n' + 'You:  '+ input
		Poori_Baat = Poori_Baat + '\n' + Jawab
		ScrlBar.configure(state='normal')
		ScrlBar.delete(0.0, END)
		ScrlBar.insert(INSERT,Poori_Baat)
		ScrlBar.see("end")
		ScrlBar.configure(state='disabled')
		lbl2.configure(text='Type your text here',fg='black')
		Text_Wala_Box.delete(0.0, END)
		Counter_Ganit = Counter_Ganit + 1

	else:
		lbl2.configure(text='Blank input provided. Kindly enter text.',fg='red')

btn = Button(window, text='Click Me',command=clicked, height = 5, width = 118, bg = 'orange',borderwidth = 0, highlightthickness = 0)
btn.grid(column=0, row=3, columnspan = 2)
window.mainloop()





