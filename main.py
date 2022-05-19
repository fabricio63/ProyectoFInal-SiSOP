import threading
import time
import logging
from sql import insert_actress,insert_movie
from multiprocessing import Queue
from scrapping import get_actresses,get_movies



logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 20
#q es el queue que va a ser el buffer de espacio limitado
q = Queue(BUF_SIZE)
#list_of_used es la lista de actrices que ya entraron al buffer, aqui se maneja que no entren repetidas al buffer
list_of_used = []

#clase de producer con sus atributos y su funcion run
class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None): 
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name
        # se realiza el webscrapping y se obtiene lista de actrices
        self.lista_actrices = get_actresses('https://en.wikipedia.org/wiki/List_of_American_film_actresses')
    def run(self):
        while True:
            if not q.full():
                if self.lista_actrices:
                    # en este while es donde se agarra un item y se asegura que el item escogido sea unico
                    value = True
                    while value == True:
                        try:

                            # se puede elegir random o en orden

                            # item = random.choice(self.lista_actrices)
                            item = self.lista_actrices[0]
                            self.lista_actrices.remove(item)
                            if item not in list_of_used:
                                list_of_used.append(item)
                                value = False
                        except:
                            pass
                    # item.append(self.name)
                   
              
                    q.put((item,self.name))
                    
                    logging.debug('Putting ' + str(item)  
                                + ' : ' + str(q.qsize()) + ' items in queue')
                    time.sleep(0.01)
        return
#clase de consumer y sus funciones y atributos
class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item,producername = q.get()
                #agraga el consumidor y el productor a la lista item
                item.append(producername)
                item.append(self.name)
                try:
                    #se llama la funcion insert_actress que mete la actriz a la tabla en sql
                    insert_actress(item)
                except:
                    pass
                movies = get_movies(item[1])
                try:
                    #se inserta a la tabla de peliculas en sql y se inserta las referencia a la tabla de actricesypeliculas
                    insert_movie(movies,self.name,item[0])
                except:
                    pass
                
                logging.debug('Getting ' + str(item) 
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(0.01)
        return

if __name__ == '__main__':
    #se instancias los productores y consumidores
    p1 = ProducerThread(name='producer1')
    c1 = ConsumerThread(name='consumer1')
    p2 = ProducerThread(name='producer2')
    c2 = ConsumerThread(name='consumer2')
    p3 = ProducerThread(name='producer3')
    c3 = ConsumerThread(name='consumer3')
    p4 = ProducerThread(name='producer4')
    c4 = ConsumerThread(name='consumer4')

    #se inician los consumidores y productores
    c1.start()
    c2.start()
    c3.start()
    c4.start()
    # time.sleep(2)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    # time.sleep(10)