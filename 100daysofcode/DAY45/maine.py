import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
all_mov = soup.find_all(name="h3", class_="title")
mov_list = [mov.getText() for mov in all_mov]
mov_list.reverse()
print(mov_list)

with open("movies.txt", mode="w") as file:
    for mov in mov_list:
        file.write(f"{mov}\n")


