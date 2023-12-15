from tkinter import *
from tkinter import messagebox
from PyDictionary import PyDictionary

root = Tk()
root.title("Dictionary")
root.geometry("500x400")

dictionary = PyDictionary()

def getMeaning():
    response = dictionary.meaning(word.get())
    if(response):
        if('Noun' in response):
            meaning =response['Noun'][0]
        elif('Verb' in response):
            meaning = response['Verb'][0]

        elif('Adjective' in response):
            meaning = response['Adjective'][0]

        else:
            meaning="Invalid word"
    else:
        messagebox.showinfo("Error","Please add a Noun,Pronoun,verb or a valid word.")
    meaning_label.config(text=meaning)
