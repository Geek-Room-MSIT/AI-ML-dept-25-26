#importing tkinter and message box
from tkinter import *
import tkinter.messagebox as msgb

#creating the window
task1 = Tk()
#Window details like the title of the window and size
task1.title("Task 1")
task1.geometry("1280x720")
task1.minsize(120,180)

#now we create a dictionary with negative and postive emojies and text with some appropriate value.
mood_dict={"happy":1, "cheerful":1, "joyful":1, "excited":1, "content":1, "wonderful":1, "delighted":1, "blessed":1,"😊":1, "😁":1, "😄":1, "😂":1, "🥳":1, "😍":1, "🤩":1, "🎉":1,"sad":-1, "unhappy":-1, "down":-1, "depressed":-1, "gloomy":-1, "miserable":-1, "blue":-1, "low":-1,"😞":-1, "😢":-1, "😭":-1, "😔":-1, "😿":-1, "😩":-1, "😟":-1}

#now to create a heading which says mood detector
Label(text="Mood Detector", font="Robotomono 26 bold").pack(padx=10)

#defining the exit command
def Exit():
    exit_value=msgb.askyesnocancel("End Program?","Do you wan to exit this program?")
    if exit_value==True:
        task1.quit()

#now a menu to exit the software
toolbar=Menu(task1)
toolbar.add_command(label="End Program",command=Exit)
task1.config(menu=toolbar)


#just a small description kinda thing
Label(text="Enter a string below and based on the words and emojis this software will decide if the sentence was positive, negative or neutral <3").pack(padx=10)

#input the string
SentenceVar=StringVar()
Entry(task1,textvariable=SentenceVar,width=100).pack(padx=10)

#now collecting the Sentence and adding a submit button and calculating the mood
def submit():
    Sentence=SentenceVar.get()
    words=Sentence.split()
    mood=0
    for i in words:
        if i in mood_dict:
            mood+=mood_dict[i]
    #now to display the mood
    if mood==0:
        msgb.showinfo("Your Mood","Neutral Mood")
    elif mood>0 and mood<5:
        msgb.showinfo("Your Mood","Good Mood!")
    elif mood>5:
        msgb.showinfo("Your Mood","Extremely Great Mood")
    elif mood<0 and mood>-5:
        msgb.showinfo("Your Mood","Bad Mood")
    elif mood<-4:
        msgb.showinfo("Your Mood","Extremely Bad Mood")
    else:
        msgb.showinfo("Error!","Oops! Something Unexpected occured :<")
ButtonFrame=Frame(task1,borderwidth=3).pack(padx=10)
Button(ButtonFrame,text="Check mood!",command=submit).pack(padx=12)




task1.mainloop()
