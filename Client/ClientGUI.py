from tkinter import *
from customtkinter import *
from tkinter.messagebox import showerror
from threading import Thread
import requests
import json

import Data

class AsyncAPI(Thread):
    def __init__(self, url):
        super().__init__()


    def run(self):
        JsonObj = json.dumps(Data.Process)
        response = requests.post("https://httpbin.org/post",JsonObj)
        print(response)

class App(Tk):
    #Globale Variablen
     #Variablen Initiieren
    processSubPageCount = 0

    #Konstruktor
    def __init__(self):
        super().__init__()

        self.title('ClientGUI')
        #self.attributes("-fullscreen", True)
        self.geometry("1240x600")


        #Aufbau GUI
        self.drawNavBar()
        self.drawProcessPage()

    #NavBar zum wechseln der Seiten
    def drawNavBar(self):
        self.navBar = Frame(master=self,bg="#97a5b0",width=200, height=700).place(x=0,y=0)
        self.processButton = CTkButton(master=self.navBar,text="Process",corner_radius=10,width=150,height=50,command=lambda:self.changePage("processPage")).place(relx=0.08,rely=0.2, anchor=CENTER)
        self.materialButton = CTkButton(master=self.navBar,text="Material",corner_radius=10,width=150,height=50,command=lambda:self.changePage("materialPage")).place(relx=0.08,rely=0.4, anchor=CENTER)
        self.helpButton = CTkButton(master=self.navBar,text="HELP",corner_radius=10, width=150,height=50,command=lambda:self.changePage("helpPage")).place(relx=0.08,rely=0.6, anchor=CENTER)

    #Prozess HauptSeite (Ruft Unterseiten auf)
    def drawProcessPage(self):
        self.processPage = Frame(master=self,bg="#ffffff",width=1040, height=700).place(x=200,y=0)
        self.processLabel = Label(master=self.processPage, text="Process",bg="#ffffff",fg="#505559",font=("Century Gothic",30,"bold underline")).place(relx=0.6,rely=0.1, anchor=CENTER)
        self.previousPage = CTkButton(master=self.processPage, text="Prev.",bg_color="#ffffff",fg_color="#97a5b0",hover_color="#505559",corner_radius=10, width=200, height=50, command=lambda: self.processSubPageCounter("Down")).place(relx=0.25,rely=0.1, anchor=CENTER)
        self.nextPage = CTkButton(master=self.processPage,text="Next",bg_color="#ffffff",fg_color="#97a5b0",hover_color="#505559",corner_radius=10, width=200, height=50, command=lambda: self.processSubPageCounter("Up")).place(relx=0.9,rely=0.1, anchor=CENTER)
        self.drawProcessSubPage()

    #Prozess Subseite
    def drawProcessSubPage(self):
        self.processSubPage = Frame(master=self.processPage,bg="#ffffff",width=1040, height=500).place(x=200,rely=0.15)
        counter = 0.05
        for key,state in Data.Process[self.processSubPageCount].items():
            counter += 0.2
            self.button = CTkButton(master=self.processSubPage,text=key,bg_color="#ffffff",fg_color="#97a5b0",hover_color="#505559",corner_radius=10, width=600, height=100, state=state,command=lambda:self.handelButtonPress(key)).place(relx=0.6,rely=counter, anchor=CENTER)

    def processSubPageCounter(self,action):
        if action == "Up":
            self.processSubPageCount += 1
        elif action == "Down":
            self.processSubPageCount -= 1
        else:
            print("Error: processSubPageCounter")

        if self.processSubPageCount < 0:
            self.processSubPageCount = 0
        if self.processSubPageCount == len(Data.Process):
            self.processSubPageCount = len(Data.Process) -1

        self.drawProcessSubPage()

    #Material Hautpseite (Ruft Unterseiten auf)
    def drawMaterialPage(self):
        self.materialPage = Frame(master=self,bg="#ffffff",width=1040, height=700).place(x=200,y=0)
        self.materialLabel = Label(master=self.processPage, text="Material",bg="#ffffff",fg="#505559",font=("Century Gothic",30,"bold underline")).place(relx=0.6,rely=0.1, anchor=CENTER)
    
    #Hilfeseite
    def drawHelpPage(self):
        self.helpPage = Frame(master=self,bg="#ffffff",width=1040, height=700).place(x=200,y=0)
        self.helpLabel = Label(master=self.processPage, text="Help",bg="#ffffff",fg="#505559",font=("Century Gothic",30,"bold underline")).place(relx=0.6,rely=0.1, anchor=CENTER)
    
    #Einstellungen (Server IP / etc.)
    def drawSettingPage(self):
        self.settingPage = Frame(master=self,bg="#ffffff",width=1040, height=700).place(x=200,y=0)
        self.settingLabel = Label(master=self.processPage, text="Settings",bg="#ffffff",fg="#505559",font=("Century Gothic",30,"bold underline")).place(relx=0.6,rely=0.1, anchor=CENTER)
    
    #Herunterfaher des gesamten Systems (+ Rückstellung Variablen)
    def shutdownPage(self):
        pass

    #Wechselt die Hauptseiten
    def changePage(self,page):
    
        if page == "processPage":
            self.drawProcessPage()
        
        elif page == "materialPage":
            self.drawMaterialPage()

        elif page == "helpPage":
            self.drawHelpPage()

        else:
            print("Error: Could not resolve request")

    def handelButtonPress(self,key):
        AsyncAPI.run(self)

#Ausführung der App
if __name__ == "__main__":
    app = App()
    app.mainloop()