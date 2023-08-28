from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, 'html.parser')

movie_headings = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movie_headings]
movie_list.reverse()
with open ("must_watch_movies.txt", mode="w", encoding="utf-8") as movie_file:
    for movie in movie_list:
        movie_file.write(f"{movie}\n")
