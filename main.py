from tkinter import *
from textblob import TextBlob

window = Tk()
window.title("Spell Checker")
window.geometry("700x400")
window.config(bg="#191d2b")

def check_spelling():
    word_input = search_bar.get()
    word = TextBlob(word_input)
    correct_word = str(word.correct()).capitalize()
    correction = Label(window, text = "Correction: ", font = ("poppins", 20), bg = "#191d2b", fg = "white")
    correction.place(x = 100, y = 250)
    spell.config(text = correct_word, bg = "white")

heading = Label(window, text = "Spell Checker", font = ("arial", 30, "bold"), bg = "#191d2b", fg = "white")
heading.pack(pady = (50, 0))

search_bar = Entry(window, justify = "center", width = 30, font = ("poppins", 25), bg = "white", fg = "blue", border = 5)
search_bar.pack(pady = 10)
search_bar.focus()

button = Button(window, text = "Check", font = ("arial", 20, "bold"), fg = "#191d2b", bg = "white", command = check_spelling)
button.pack()

spell = Label(window, font = ("poppins", 20), bg = "#191d2b", fg = "blue")
spell.place(x = 210, y = 250)

window.mainloop()