import tkinter as tk
import random as rand
import os
from threading import Timer
from pathlib import Path
import winsound as winsound
import playsound as pls 

TomaattiIkkuna=tk.Tk()

TomaattiIkkuna.title(" Tomaatti Window ")

TomaattiIkkuna.geometry("1000x500")
path = Path(__file__).resolve().parent
os.chdir(path=path)
tomatoimage = tk.PhotoImage(file="./tomaatti.png").subsample(4,4)
targetimgae = tk.PhotoImage(file="./maalitaulu.png").subsample(8,8)
keernestiimage = tk.PhotoImage(file="./kerne.png").subsample(4,4)
eernestiimage = tk.PhotoImage(file="./erne.png").subsample(4,4)
splatimage = tk.PhotoImage(file="./splat.png").subsample(8,8)
tagetimage = tk.Label(TomaattiIkkuna,width=targetimgae.width(),height=targetimgae.height(),image=targetimgae)
tomato = tk.Label(TomaattiIkkuna,image=tomatoimage)
tomato2 = tk.Label(TomaattiIkkuna,image=tomatoimage)

EernestiDict = {

}

KeernestiDict = {

}

projetile = {

}

Targetpos = {
    "x": 500,
    "y": 250,
    "targetwidth": 1,
    "targetheight": 1
}

throws = {
    
}

def reset(): 
    throws.clear()
    splat
    KeernestiProcent.configure(text="")
    EernestiProcent.configure(text="")
    Eernestiamount.configure(text="")
    KeernestiAmount.configure(text="")

EernestiStats = tk.Label(TomaattiIkkuna,text="Eernesti")
EernestiStats.place(x=900,y=20)

EernestiProcent = tk.Label(TomaattiIkkuna)
EernestiProcent.place(x=900,y=50)

Eernestiamount = tk.Label(TomaattiIkkuna)
Eernestiamount.place(x=900,y=80)

KeernestiStats = tk.Label(TomaattiIkkuna,text="Keernesti")
KeernestiStats.place(x=20,y=20)

KeernestiProcent = tk.Label(TomaattiIkkuna)
KeernestiProcent.place(x=20,y=50)

KeernestiAmount = tk.Label(TomaattiIkkuna)
KeernestiAmount.place(x=20,y=80)

Eernesti = tk.Label(TomaattiIkkuna,image=eernestiimage)
Keernesti = tk.Label(TomaattiIkkuna,image=keernestiimage)

splat = tk.Label(TomaattiIkkuna,image=splatimage)
splat2 = tk.Label(TomaattiIkkuna,image=splatimage)

Reset = tk.Button(text="Reset", command=reset)
Reset.pack()

randomspot = rand.randint(100,400)

tagetimage.place(x=500,y=250)
Keernesti.place(x=200,y=randomspot)

KeernestiDict["x"] = 200
KeernestiDict["y"] = randomspot

TomaattiIkkuna.update_idletasks()

def Placekeernesti():
    randomspot = rand.randint(100,400)
    Eernesti.place(x=800,y=randomspot)
    EernestiDict["x"] = 800
    EernestiDict["y"] = randomspot

def EernestiKeernestiHit():
    print(throws)
    if(len(throws)>1):
        Keernestithrows = []
        Eernestithrows = []
        keernestisuccesses = 0
        eernestisuccesses = 0
        for value in throws:
         if(throws[value]["name"]=="Keernesti"):
             Keernestithrows.append(throws[value]["hit"])
         if(throws[value]["name"]=="Eernesti"):
             Eernestithrows.append(throws[value]["hit"])
        for kt in Keernestithrows:
            if(kt == "true"):
                keernestisuccesses = keernestisuccesses +1
        for et in Eernestithrows:
             if(et == "true"):
                eernestisuccesses = eernestisuccesses +1
        if(keernestisuccesses>0):
            procent = round(keernestisuccesses/len(Keernestithrows)*100,3)
            KeernestiProcent.configure(text=str(procent))
        if(eernestisuccesses>0):
            procent = round(eernestisuccesses/len(Eernestithrows)*100,3)
            EernestiProcent.configure(text=str(procent))

        KeernestiAmount.configure(text=str(len(Keernestithrows)))
        Eernestiamount.configure(text=str(len(Eernestithrows)))
        





def tomatoanimationKeernesti():
    KeernestiTimer = Timer(0.01,tomatoanimationKeernesti)
    KeernestiTimer.start()
    win = 0
    if(projetile[1]["x"]>projetile[1]["throwx"]):
        projetile[1]["x"] = projetile[1]["x"]-1
    if(projetile[1]["x"]<projetile[1]["throwx"]):  
        projetile[1]["x"] = projetile[1]["x"]+1
    if(projetile[1]["y"]>projetile[1]["throwy"]):
        projetile[1]["y"] = projetile[1]["y"]-1
    if(projetile[1]["y"]<projetile[1]["throwy"]):  
        projetile[1]["y"] = projetile[1]["y"]+1
    tomato2.place(x=projetile[1]["x"],y=projetile[1]["y"])
    if(projetile[1]["x"]==projetile[1]["throwx"] and projetile[1]["y"]==projetile[1]["throwy"]):
        splat2.place(x = projetile[1]["throwx"], y = projetile[1]["throwy"])
        TomaattiIkkuna.update_idletasks()
        splatwidth = splat2.winfo_x() + splat2.winfo_width()
        splatheight = splat2.winfo_y() + splat2.winfo_height()
        print(splatheight, "  ", splatwidth)
        print(Targetpos["targetwidth"], "  ", Targetpos["targetheight"])
        if (splat2.winfo_x() < Targetpos["targetwidth"] and splatwidth > tagetimage.winfo_x() and
            splat2.winfo_y() < Targetpos["targetheight"] and splatheight > tagetimage.winfo_y()):

            print("true")
            print(len(throws))
            throws[len(throws)+1] = {
                "name": "Keernesti",
                "hit": "true",
                "x": splat.winfo_x(),
                "y":  splat.winfo_y()
            }
            win = 1
        else:
            print("false")
            print(len(throws))
            throws[len(throws)+1] = {
                "name": "Keernesti",
                "hit": "false",
                "x": splat.winfo_x(),
                "y":  splat.winfo_y()
            }

        tomato2.place_forget()
        KeernestiTimer.cancel()
        if(win): 
            wins()
        EernestiKeernestiHit()

def PlaceKeernestiTomato():

    value = calculatethrow()
    projetile[1] = {"x": KeernestiDict["x"]+20, "y": KeernestiDict["y"],"throwx": value[0], "throwy": value[1]}
    tomato2.place(x=projetile[1]["x"], y=projetile[1]["y"])
    tomatoanimationKeernesti()

def calculatethrow():

    x = rand.randint(Targetpos["x"]-60,Targetpos["x"]+60)
    y = rand.randint(Targetpos["y"]-60,Targetpos["y"]+60)
    return x,y

def wins():
    winsound.Beep(40,80)

def tomatoanimationEernesti():

    timer = Timer(0.01,tomatoanimationEernesti)
    timer.start()
    win = 0
    if(projetile[0]["x"]>projetile[0]["throwx"]):
        projetile[0]["x"] = projetile[0]["x"]-1
    if(projetile[0]["x"]<projetile[0]["throwx"]):  
        projetile[0]["x"] = projetile[0]["x"]+1
    if(projetile[0]["y"]>projetile[0]["throwy"]):
        projetile[0]["y"] = projetile[0]["y"]-1
    if(projetile[0]["y"]<projetile[0]["throwy"]):  
        projetile[0]["y"] = projetile[0]["y"]+1
    
    tomato.place(x=projetile[0]["x"],y=projetile[0]["y"])

    if(projetile[0]["x"]==projetile[0]["throwx"] and projetile[0]["y"]==projetile[0]["throwy"]):
        splat.place(x = projetile[0]["throwx"], y = projetile[0]["throwy"])

        TomaattiIkkuna.update_idletasks()

        splatwidth = splat.winfo_x() + splat.winfo_width()
        splatheight = splat.winfo_y() + splat.winfo_height()

        print(splatheight, "  ", splatwidth)
        print(Targetpos["targetwidth"], "  ", Targetpos["targetheight"])

        if (splat.winfo_x() < Targetpos["targetwidth"] and splatwidth > tagetimage.winfo_x() and
            splat.winfo_y() < Targetpos["targetheight"] and splatheight > tagetimage.winfo_y()):

            print("true")
            print(len(throws))

            throws[len(throws)+1] = {
                "name": "Eernesti",
                "hit": "true",
                "x": splat.winfo_x(),
                "y": splat.winfo_y()
            }
            win = 1
        else:

            print("false")
            print(len(throws))

            throws[len(throws)+1] = {
                "name": "Eernesti",
                "hit": "false",
                "x": splat.winfo_x(),
                "y": splat.winfo_y()
            }
        tomato.place_forget()
        timer.cancel()
        if(win==1):
            wins()
        EernestiKeernestiHit()
    
def PlaceEernestiTomato():
    value = calculatethrow()
    projetile[0] = {"x": EernestiDict["x"]-20, "y": EernestiDict["y"],"throwx": value[0], "throwy": value[1]}
    tomato.place(x=projetile[0]["x"], y=projetile[0]["y"])
    tomatoanimationEernesti()
   


Targetpos["targetwidth"] = tagetimage.winfo_x() + tagetimage.winfo_width() - 10
Targetpos["targetheight"] = tagetimage.winfo_y() + tagetimage.winfo_height() - 10



ButtonKeernesti = tk.Button(text="KeernestiPlacer",command=Placekeernesti)
ButtonEernestiThrow = tk.Button(text="Keernestithrow",command=PlaceKeernestiTomato)
ButtonKeernestiThrow = tk.Button(text="EernestiThrow",command=PlaceEernestiTomato)
ButtonKeernesti.pack()
ButtonEernestiThrow.pack()
ButtonKeernestiThrow.pack()
TomaattiIkkuna.mainloop()