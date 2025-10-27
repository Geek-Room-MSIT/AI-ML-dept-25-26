#importing modules
import random as r
from tkinter import *
import tkinter.messagebox as msgb

#creating the main window
Mainwindow=Tk()
#defining thw window geometry
Mainwindow.title("Treasure hunt")
Mainwindow.geometry("1280x720")
Mainwindow.minsize(120,180)
Mainwindow.configure(bg="lightgrey")

#heading and description
Label(Mainwindow,text="🎉🗺️ Treasure Hunt 🏴‍☠️✨",font="Robotomono 26 bold").pack(padx=10)
Label(Mainwindow,text="This is a treasure hunt where the treasure is hidden behind a random box.\n\nYou have 3 guesses to find out where the treasure is.\n\n Good Luck! (;",activebackground="red").pack(padx=10,pady=15)

#creating the answer
ans=r.randint(1,5)
tries=3
#creating a frame for the trasure chests
trasureframe=Frame(Mainwindow,height=250)
trasureframe.pack(pady=20,fill=X,expand=True)
#adding the trasure chest as a button
trasurechest=PhotoImage(file="Sreenandh_S\\task-3\\treasurechest.jpeg")

def chest1():
    retry=game_over()
    global tries , ans
    if retry==True:
        if ans==1:
            play_again=msgb.askyesno("Congratulations!","You have found the Treasure!!\nDo you want to play again?")
            if play_again==True:
                ans=r.randint(1,5)
                tries=3
            else:
                Mainwindow.quit()
        elif ans>1:
            msgb.showinfo("HINT","To your right")
            tries-=1
    else:
        Mainwindow.quit()
    
def chest2():
    retry=game_over()
    global tries , ans
    if retry==True:
        if ans==2:
            play_again=msgb.askyesno("Congratulations!","You have found the Treasure!!\nDo you want to play again?")
            if play_again==True:
                ans=r.randint(1,5)
                tries=3
            else:
                Mainwindow.quit()
        elif ans<2:
            tries-=1
            msgb.showinfo("HINT","To your left")
        elif ans>2:
            tries-=1
            msgb.showinfo("HINT","To your Right")
    else:
        Mainwindow.quit()

def chest3():
    retry=game_over()
    global tries , ans
    if retry==True:
        if ans==3:
            play_again=msgb.askyesno("Congratulations!","You have found the Treasure!!\nDo you want to play again?")
            if play_again==True:
                ans=r.randint(1,5)
                tries=3
            else:
                Mainwindow.quit()
        elif ans<3:
            tries-=1
            msgb.showinfo("HINT","To your left")
        elif ans>3:
            tries-=1
            msgb.showinfo("HINT","To your right")
    else:
        Mainwindow.quit()
def chest4():
    retry=game_over()
    global tries , ans
    if retry==True:
        if ans==4:
            play_again=msgb.askyesno("Congratulations!","You have found the Treasure!!\nDo you want to play again?")
            if play_again==True:
                ans=r.randint(1,5)
                tries=3
            else:
                Mainwindow.quit()
        elif ans<4:
            tries-=1
            msgb.showinfo("HINT","To your left")
        elif ans>4:
            tries-=1
            msgb.showinfo("HINT","To your right")
    else:
        Mainwindow.quit()
def chest5():
    retry=game_over()
    global tries , ans
    if retry==True:
        if ans==5:
            play_again=msgb.askyesno("Congratulations!","You have found the Treasure!!\nDo you want to play again?")
            if play_again==True:
                ans=r.randint(1,5)
                tries=3
            else:
                Mainwindow.quit()
        elif ans<5:
            tries-=1
            msgb.showinfo("HINT","To your left")
        elif ans>5:
            tries-=1
            msgb.showinfo("HINT","To your right")
    else:
        Mainwindow.quit()
def game_over():
    global tries
    if tries==0:
        retry=msgb.askyesno("Better Luck Next Time","You couldn't find the trasure in 3 tries.\nDo you want to play again?")
        if retry==True:
            ans=r.randint(1,5)
            tries=3
            return True
        else:
            Mainwindow.quit()
            return False
    else:
        return True


chest1_button=Button(trasureframe,image=trasurechest,command=chest1,width=115,height=120)
chest1_button.grid(row=0,column=2,padx=50)
chest2_button=Button(trasureframe,image=trasurechest,command=chest2,width=115,height=120)
chest2_button.grid(row=0,column=1,padx=50)
chest3_button=Button(trasureframe,image=trasurechest,command=chest3,width=115,height=120)
chest3_button.grid(row=0,column=3,padx=50)
chest4_button=Button(trasureframe,image=trasurechest,command=chest4,width=115,height=120)
chest4_button.grid(row=0,column=4,padx=50)
chest5_button=Button(trasureframe,image=trasurechest,command=chest5,width=115,height=120)
chest5_button.grid(row=0,column=5,padx=50)

Mainwindow.mainloop()
