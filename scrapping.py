
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
    listado_peliculasf = []
    try:
        mydivs = soup.find(id="Filmography").find_next('ul').find_next('ul')

        mydivs1 = soup.find(id="Filmography").find_next('table')
        
        # print(mydivs)

        filmography = mydivs.findAll('a')
        
        
        for i in filmography:
            title = i.get('title')
            link = 'https://en.wikipedia.org'+i.get('href')
            if 'Category':
                if '/wiki/'in link:
                
                    listado_peliculas.append([title,link])

        filmography1 = mydivs1.findAll('a')
        
        
        for i in filmography1:
            title = i.get('title')
            
            link = 'https://en.wikipedia.org'+i.get('href')
            if '/wiki/'in link:
                listado_peliculas.append([title,link])
        
        
        # for i in listado_peliculas:
        #     if 'Category' in i[0]:
        #         pass
        #     else:   
        #         listado_peliculasf.append(i)

        return listado_peliculas
    except:
        pass
        
# if 'Category' not in title and 'ISNI' not in title and 'VIAF' not in title and 'Wikidata' not in title  and 'Authority control' not in title :        
# print(get_movies('https://en.wikipedia.org/wiki/Lola_Falana'))
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