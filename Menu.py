from tkinter import *
import tkinter as tk

# defines functions for buttons
def playGame():

    print("plays game")


def charSelect():
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    title.place(x=105, y=50)
    backButton.place(x=560, y=500)

def about():
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    title.place(x=105, y=50)
    aboutText.place(x=390, y=200)
    backButton.place(x=560, y=500)

def back():
    title.place(x=105, y=100)
    playButton.place(x=560, y=350)
    characterButton.place(x=560, y=425)
    aboutButton.place(x=560, y=500)
    currentChar.place(x=50, y=400)
    aboutText.place_forget()
    backButton.place_forget()

def charImage(colour):
    # resized char sprites
    if colour == "blue":
        charImage = tk.PhotoImage(file="images\\blue\\blue.png")
        return charImage
    elif colour == "orange":
        charImage = tk.PhotoImage(file="images\\orange\\orange.png")
        return charImage
    elif colour == "purple":
        charImage = tk.PhotoImage(file="images\\purple\\purple.png")
        return charImage
    elif colour == "red":
        charImage = tk.PhotoImage(file="images\\red\\red.png")
        return charImage

# open window for application
app = Tk()
app.title('Adolescent Deformed Samurai Tortoises')
app.geometry("1280x600+30-100")

aboutText = Label(app, text="AI Pathing - Hunter Britton\n"
                                "Front-End GUI - Alexander Lay\n"
                                "Animation Engine - Noah Nogueira\n"
                                "Game Engine - Fahim Zaman\n\n"
                                "THANKS FOR PLAYING!", bg="#008000", fg="#F5F5F5", font=('Arial', 24))
backButton = Button(app, text="BACK", bg="#006400", fg="#F5F5F5", command=back)
backButton.config(height=3, width=20)

# title label
title = Label(app, text="Adolescent Deformed Samurai Tortoises", bg="#008000", fg="#F5F5F5", font=('Comic Sans MS', 42))
title.place(x=105, y=100)

# current character
currentChar = Label(app, text="Current Character:", bg="#008000", fg="#F5F5F5")
currentChar.config(height=1, width=25)
currentChar.place(x=50, y=400)

currentColour = "blue"
currentCharImage = charImage(currentColour)
currentCharLabel = Label(image=currentCharImage)
currentCharLabel.place(x=50, y=250)

# play button
playButton = Button(app, text="PLAY", bg="#006400", fg="#F5F5F5", command=playGame)
playButton.config(height=3, width=20)
playButton.place(x=560, y=350)

# character button
characterButton = Button(app, text="CHARACTER SELECT", bg="#006400", fg="#F5F5F5", command=charSelect)
characterButton.config(height=3, width=20)
characterButton.place(x=560, y=425)

# about button
aboutButton = Button(app, text="ABOUT", bg="#006400", fg="#F5F5F5", command=about)
aboutButton.config(height=3, width=20)
aboutButton.place(x=560, y=500)

app.mainloop()