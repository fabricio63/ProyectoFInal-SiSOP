# Proyecto Final Sistemas Operativos

## Acerca del Proyecto

Almacenar en una base de datos la relación existente entre películas y actrices. El objetivo es leer el HTML del sitio de actrices y almacenar lo que se le indica en una base de datos mysql.

URL a escanear:
https://en.wikipedia.org/wiki/List_of_American_film_actresses

El proyecto está compuesto de 2 piezas de software.
* Productores: El sistema crea 4 hilos encargados de realizar el scraping del html de la actriz. El elemento a producir debe de ser almacenado en un buffer de tamaño limitado. (“Problema del buffer limitado”). El elemento a almacenar contiene el nombre y el URL de la actriz a procesar por un consumidor. 

* Consumidor:  El programa debe de crear 4 procesos consumidores, estos procesos son el encargado de ingestar en una BD la información de la actriz y las películas en las que ha actuado. Si la actriz ya está siendo procesada o ya fue procesada el proceso del consumidor descartará el elemento y necesitará competir por otro elemento. “debe continuar con otra actriz”

_Las actrices y las películas no pueden estar repetidas en la BD_

## Para ejecutar el código
```
Ejecutar main.py 
** Asegurarse de que sql.py y scrapping.py estén en la misma carpeta que main.py **
```

## Librerias utilizadas
```
peewee: se utiliza como orm para base de datos
threading: se utiliza para la implementación de consumidor y productor
time: para utilización de sleeps
logging: se utiliza para prints en la terminal 
scrapping: utiliza beuatiful soup para el scrapping de las páginas
request: se utiliza para obtener el código fuente de las páginas de wikipedia
```

## Web Scrapping
Se tienen dos funciones:
* La función `get_actresses()` requiere el link principal. Se encarga de obtener todas las actrices. Luego, almacena el nombre de la actriz y su link de wikipedia.
* La función `get_movies()` utiliza el link de cada actriz y obtiene las películas y los links respectivos del área de "Filmography".

En caso una actriz o película no tenga un link de Wikipedia, no se agrega a ninguna lista.

## SQL 
Se tienen tres tablas, actrices, peliculas y ActricesyPeliculas.

Las funciones para rellenar estas tablas son:
* La función `insert_actress()`, esta agrega el nombre de la actriz, el link, el nombre del productor y del consumidor. 
* La función `insert_actricesypeliculas()` en esta se agrega el nombre de la actriz, de la película y del consumidor
* La función `insert_movie()`, itera sobre una lista de películas y links. En cada iteración intenta insertar la instancia a la tabla de películas y a la tabla de peliculas y actrices. En caso de un error, significa que la película ya existe, por lo que solo agrega a la tabla de peliculas y actrices, como decir una actriz nueva en una película existente.

## Productores y Consumidores
#### Productores
Al principio, cada productor hace scrapping y cada uno obtiene su lista con todas las actrices ya que la lista de actrices es un atributo de la clase productor. 

Proceso:
- Función `run`: Elige el item 0 de la lista de actrices, lo elimina de la lista de actrices, procede a revisar que en la lista list_of_used no se encuentre dicho item.
- Si el item no se encuentra en la lista list_of_used, lo agrega a dicha lista y lo agrega al queue.
- De lo contrario, repite el proceso hasta encontrar un item que no este en list_of_usef.

#### Consumidores
Los consumidores empiezan a consumir si se cumple la condición de si el queue (buffer) no está vacío. Cada consumidor cumple con el proceso completo para empezar con otro item. 

Proceso:
1. Se llama a la función `insert_actress`
2. Llama a la función  `get_movies`
3. llamar la función `insert_movie`, dicha función agrega a la tabla de fact de películas y actrices.







