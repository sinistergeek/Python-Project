from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

s = requests.session()
films = []
names = []
ratings = []
genres = []

path = input("Enter the path where your films are:")
filmswe = os.listdir(path)
for film in filmswe:
    films.append(os.path.splitex(film)[0])

for line in films:
    title = line.lower()
