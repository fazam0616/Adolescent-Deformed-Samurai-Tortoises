from tkinter import *
import tkinter as tk

# default character
currentColour = "blue"

# defines functions for buttons
def playGame():
    print("plays game")

def charSelect():
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    currentCharLabel.place_forget()

    global mikeyButton, raphButton, donButton, leoButton
    mikeyButton = Button(app, text="MIKEY\nWeapon:\nNunchucks",
                        bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charChoice("orange"))
    mikeyButton.config(height=3, width=12)
    mikeyButton.place(x=100, y=390)
    raphButton = Button(app, text="RAPH\nWeapon:\nSai",
                        bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charChoice("red"))
    raphButton.config(height=3, width=12)
    raphButton.place(x=395, y=390)
    donButton = Button(app, text="DON\nWeapon:\nStaff",
                        bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charChoice("purple"))
    donButton.config(height=3, width=12)
    donButton.place(x=700, y=390)
    leoButton = Button(app, text="LEO\nWeapon:\nKatana",
                        bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charChoice("blue"))
    leoButton.config(height=3, width=12)
    leoButton.place(x=995, y=390)

    title.place(x=105, y=50)
    backButton.place(x=560, y=500)

def charChoice(colour):
    global currentColour
    currentColour = colour

def about():
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    currentCharLabel.place_forget()
    title.place(x=105, y=50)
    aboutText.place(x=390, y=200)
    backButton.place(x=560, y=500)

def back():
    title.place(x=105, y=100)
    playButton.place(x=560, y=350)
    characterButton.place(x=560, y=425)
    aboutButton.place(x=560, y=500)
    currentChar.place(x=120, y=350)
    currentCharLabel.place(x=125, y=375)
    backButton.place_forget()
    try:
        mikeyButton.place_forget()
        raphButton.place_forget()
        donButton.place_forget()
        leoButton.place_forget()
    except:
        aboutText.place_forget()

def charImage(colour):
    # resized char sprites
    if colour == "blue":
        charImage = tk.PhotoImage(file="images\\blue\\blueTitle.png")
        return charImage
    elif colour == "orange":
        charImage = tk.PhotoImage(file="images\\orange\\orangeTitle.png")
        return charImage
    elif colour == "purple":
        charImage = tk.PhotoImage(file="images\\purple\\purpleTitle.png")
        return charImage
    elif colour == "red":
        charImage = tk.PhotoImage(file="images\\red\\redTitle.png")
        return charImage

# open window for application
app = Tk()
app.title('Adolescent Deformed Samurai Tortoises')
app.geometry("1280x600+30-100")

backgroundImage = tk.PhotoImage(file="images\\world.png")
backgroundLabel = Label(image=backgroundImage)
backgroundLabel.place(x=10, y=0)

# button objects
aboutText = Label(app, text="AI Pathing - Hunter Britton\n"
                            "Front-End GUI - Alexander Lay\n"
                            "Animation Engine - Noah Nogueira\n"
                            "Game Engine - Fahim Zaman\n\n"
                            "THANKS FOR PLAYING!", bg="#008000", fg="#F5F5F5", font=('Arial', 24))

# title label
title = Label(app, text="Adolescent Deformed Samurai Tortoises", bg="#008000", fg="#F5F5F5", font=('Comic Sans MS', 42))
title.place(x=105, y=100)

# back button
backButton = Button(app, text="BACK", bg="#006400", fg="#F5F5F5", command=back)
backButton.config(height=3, width=20)

# current character
currentChar = Label(app, text="Current Character:", bg="#006400", fg="#F5F5F5")
currentChar.config(height=1, width=25)
currentChar.place(x=120, y=350)

currentCharImage = charImage(currentColour)
currentCharLabel = Label(image=currentCharImage, bg="#006400")
currentCharLabel.place(x=125, y=375)

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