
from bs4 import BeautifulSoup
import requests
URL = "https://en.wikipedia.org/wiki/List_of_American_film_actresses"

# funcion de webscrapping para las actrices 
def get_actresses(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    #busca el espacio de html mw-content-text y luego busca todas las listas no ordenadas
    uls = soup.find(id="mw-content-text").findAll("ul")
    #div de cada letra del abecedario 
    mydivs = soup.find_all("div", {"class": "div-col"})
    my_list = []
    substring = 'page does not exist'
    # itera en cada div, encuentra todos los li luego encuentra todos los tipo a y de ahi saca la informacion title y link
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

    # se realiza un try si en dado caso no llega a encontrar informacion 
    try:
        #mydivs es el que encuentra listas de peliculas de tipo ul
        mydivs = soup.find(id="Filmography").find_next('ul').find_next('ul')

        #mydivs1 se encarga de encontrar las peliculas que esten dentro de el tipo table
        mydivs1 = soup.find(id="Filmography").find_next('table')
        
  
        # aqui se itera sobre todos los tipo a que esten dentro de la ul que encontramos
        filmography = mydivs.findAll('a')
        
        
        for i in filmography:
            title = i.get('title')
            link = 'https://en.wikipedia.org'+i.get('href')
            if 'Category':
                if '/wiki/'in link:
                
                    listado_peliculas.append([title,link])

        # aqui se itera sobre todos los tipo a que esten dentro de la tabla que encontramos
        filmography1 = mydivs1.findAll('a')
        
        
        for i in filmography1:
            title = i.get('title')
            
            link = 'https://en.wikipedia.org'+i.get('href')
            if '/wiki/'in link:
                listado_peliculas.append([title,link])
        
        
     

        return listado_peliculas
    except:
        pass
        
