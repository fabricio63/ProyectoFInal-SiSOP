
from bs4 import BeautifulSoup
import requests
URL = "https://en.wikipedia.org/wiki/List_of_American_film_actresses"
def get_actresses(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    uls = soup.find(id="mw-content-text").findAll("ul")
    mydivs = soup.find_all("div", {"class": "div-col"})
    my_list = []
    substring = 'page does not exist'
    for i in mydivs:
        for li in i.findAll('li'):
            for a in li.findAll('a'):
                title = a.get('title')
                link = 'https://en.wikipedia.org' + a.get('href')
                if title != None and substring not in title:
                    lista = [title,link]
                    my_list.append(lista)
    return my_list       
        
test = get_actresses(URL)


def get_movies(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    listado_peliculas = []
    try:
        mydivs = soup.find(id="Filmography").find_next('table')
        filmography = mydivs.findAll('a')
        
        
        for i in filmography:
            title = i.get('title')
            link = 'https://en.wikipedia.org'+i.get('href')
            listado_peliculas.append([title,link])
        return listado_peliculas
    except:
        pass
print(get_movies('https://en.wikipedia.org/wiki/Jeanne_Carmen'))
# for i in test:
#     lista = get_movies(i[1])
#     print(lista)




# def get_movies(link):
#     page = requests.get(link)
#     soup = BeautifulSoup(page.content, "html.parser")
#     mydivs = soup.find(id="mw-content-text").findAll("table")

#     filmography = mydivs[1].findAll('a')
    
#     for i in filmography:
#         title = i.get('title')
#         link = i.get('href')
#         print(title)