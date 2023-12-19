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
    query = "+".join(title.split())
    URL = "https://www.imdb.com/search/title/?title="+query
    print(URL)
    try:
        response =s.get(URL)
        content = response.content
        soup = BeautifulSoup(response.content,features="html.parser")
        containers = soup.find_all("div",class_="lister-item-content")
        for result in containers:
            name1 = result.h3.a.text
            name = result.h3.a.text.lower()
            if title in name:
                rating = result.find("div",class_="inline-block ratings-imdb-rating")["data-value"]
                genre = result.p.find("span",class_="genre")
                genre = genre.contents[0]
                names.append(name1)
                ratings.append(rating)
                genres.append(genre)
    except Exception:
        print("Try again with valid combination of title and release year")

df = pd.DataFrame({'Film Name':names,'Rating':ratings,'Genre':genres})
df.to_csv('film_ratings.csv',index=False,encoding='utf-8')
