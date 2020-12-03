import tkinter
from tkinter import *
from tkinter import font

# defines functions for buttons
def playGame():
    print("plays game")

def charSelect():
    print("opens character selection menu")

def about():
    playButton.place_forget()
    characterButton.place_forget()
    aboutButton.place_forget()
    currentChar.place_forget()
    title.place(x=105, y=50)

    aboutText = Label(app, text="Vector Map - Hunter Britton\n"
                                "Menus - Alexander Lay\n"
                                "Animations - Noah Nogueira\n"
                                "Controls - Fahim Zaman", bg="#008000", fg="#F5F5F5", font=('Arial', 24))
    aboutText.place(x=450, y=250)

    backButton = Button(app, text="BACK", bg="#006400", fg="#F5F5F5", command=back)
    backButton.config(height=3, width=20)
    backButton.place(x=560, y=500)

def back():
    main

# open window for application
app = Tk()
app.title('Adolescent Deformed Samurai Tortoises')
app.geometry("1280x600+30-100")

# title label
title = Label(app, text="Adolescent Deformed Samurai Tortoises", bg="#008000", fg="#F5F5F5", font= ('Comic Sans MS',42))
title.place(x=105, y=100)

# current character
currentChar = Label(app, text="Current Character:", bg="#008000", fg="#F5F5F5")
currentChar.config(height=1, width=25)
currentChar.place(x=50, y=400)

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
