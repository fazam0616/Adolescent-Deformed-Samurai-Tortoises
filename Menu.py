from tkinter import *
import tkinter as tk
import main

# defines functions for buttons
currentColour = "blue"
def playGame():
    app.wm_state('iconic')
    main.main(currentColour)
    app.wm_state('normal')

def charSelect():
    global path
    path = "characters"
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    currentCharLabel.place_forget()
    title.place_forget()

    mikeyImageLabel.place(x=105, y=25)
    raphImageLabel.place(x=400, y=25)
    donImageLabel.place(x=705, y=25)
    leoImageLabel.place(x=1000, y=25)

    mikeyButton.place(x=100, y=275)
    raphButton.place(x=395, y=275)
    donButton.place(x=700, y=275)
    leoButton.place(x=995, y=275)

    mikeyStats.place(x=86, y=400)
    raphStats.place(x=381, y=400)
    donStats.place(x=686, y=400)
    leoStats.place(x=981, y=400)

    backButton.place(x=560, y=500)

def about():
    global path
    path = "about"
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
    if path == "characters":
        backButton.place_forget()
        mikeyButton.place_forget()
        raphButton.place_forget()
        donButton.place_forget()
        leoButton.place_forget()
        mikeyImageLabel.place_forget()
        raphImageLabel.place_forget()
        donImageLabel.place_forget()
        leoImageLabel.place_forget()
        mikeyStats.place_forget()
        raphStats.place_forget()
        donStats.place_forget()
        leoStats.place_forget()
    elif path == "about":
        aboutText.place_forget()

def charImageBlue():
    global charImage, currentCharLabel, currentColour
    charImage = tk.PhotoImage(file="images\\blue\\blueTitle.png")
    currentCharImage = charImage
    currentCharLabel = Label(image=currentCharImage, bg="#006400")
    currentColour = "blue"

def charImageOrange():
    global charImage, currentCharLabel, currentColour
    charImage = tk.PhotoImage(file="images\\orange\\orangeTitle.png")
    currentCharImage = charImage
    currentCharLabel = Label(image=currentCharImage, bg="#006400")
    currentColour = "orange"

def charImagePurple():
    global charImage, currentCharLabel, currentColour
    charImage = tk.PhotoImage(file="images\\purple\\purpleTitle.png")
    currentCharImage = charImage
    currentCharLabel = Label(image=currentCharImage, bg="#006400")
    currentColour = "purple"

def charImageRed():
    global charImage, currentCharLabel, currentColour
    charImage = tk.PhotoImage(file="images\\red\\redTitle.png")
    currentCharImage = charImage
    currentCharLabel = Label(image=currentCharImage, bg="#006400")
    currentColour = "red"

# open window for application
app = Tk()
app.title('Adolescent Deformed Samurai Tortoises')
app.geometry("1280x600+30-100")

# default character
charImage = tk.PhotoImage(file="images\\blue\\blueTitle.png")

backgroundImage = tk.PhotoImage(file="images\\world.png")
backgroundLabel = Label(image=backgroundImage)
backgroundLabel.place(x=10, y=0)

# button objects
aboutText = Label(app, text="AI Pathing - Hunter Britton\n"
                            "Front-End GUI - Alexander Lay\n"
                            "Animation Engine - Noah Nogueira\n"
                            "Game Engine - Fahim Zaman\n\n"
                            "THANKS FOR PLAYING!", bg="#008000", fg="#F5F5F5", font=('Arial', 24))
mikeyButton = Button(app, text="SIMON",
                    bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charImageOrange)
mikeyButton.config(height=3, width=12)
raphButton = Button(app, text="URBINO",
                    bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charImageRed)
raphButton.config(height=3, width=12)
donButton = Button(app, text="BARDI",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charImagePurple)
donButton.config(height=3, width=12)
leoButton = Button(app, text="DA VINCI",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 18), command=charImageBlue)
leoButton.config(height=3, width=12)

mikeyStats = Label(app, text="Weapon: Nunchucks\nDamage: 2\n Speed: 8",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 15))
mikeyStats.config(height=3, width=18)
raphStats = Label(app, text="Weapon: Sai\nDamage: 7\n Speed: 1.5",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 15))
raphStats.config(height=3, width=18)
donStats = Label(app, text="Weapon: Staff\nDamage: 4\n Speed: 6",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 15))
donStats.config(height=3, width=18)
leoStats = Label(app, text="Weapon: Katana\nDamage: 5\n Speed: 3",
                   bg="#008000", fg="#F5F5F5", font=('Arial', 15))
leoStats.config(height=3, width=18)

char1Image = tk.PhotoImage(file="images\\orange\\orangeTitle.png")
mikeyImage = char1Image
mikeyImageLabel = Label(image=mikeyImage, bg="#006400")
char2Image = tk.PhotoImage(file="images\\red\\redTitle.png")
raphImage = char2Image
raphImageLabel = Label(image=raphImage, bg="#006400")
char3Image = tk.PhotoImage(file="images\\purple\\purpleTitle.png")
donImage = char3Image
donImageLabel = Label(image=donImage, bg="#006400")
char4Image = tk.PhotoImage(file="images\\blue\\blueTitle.png")
leoImage = char4Image
leoImageLabel = Label(image=leoImage, bg="#006400")

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

currentCharImage = charImage
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