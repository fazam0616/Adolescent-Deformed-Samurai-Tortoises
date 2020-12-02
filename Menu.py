import tkinter
from tkinter import *

# defines functions for buttons
def playGame():
    print("plays game")

# open window for application
app = tkinter.Tk()
app.title('Adolescent Deformed Samurai Tortoises')
app.geometry("1280x600+25-100")

# play button
playButton = tkinter.Button(app, text="PLAY", bg="#006400", fg="#F5F5F5", command=playGame)
playButton.config(height=3, width=20)
playButton.pack()

# character button
characterButton = tkinter.Button(app, text="CHARACTER SELECT", bg="#006400", fg="#F5F5F5", command=playGame)
characterButton.config(height=3, width=20)
characterButton.pack()

app.mainloop()
