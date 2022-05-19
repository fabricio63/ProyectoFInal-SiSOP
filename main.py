import threading
import time
import logging
from sql import insert_actress,insert_movie
from multiprocessing import Queue
from scrapping import get_actresses,get_movies



logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 20
q = Queue(BUF_SIZE)
list_of_used = []
class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None): 
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name
        self.lista_actrices = get_actresses('https://en.wikipedia.org/wiki/List_of_American_film_actresses')
    def run(self):
        while True:
            if not q.full():
                if self.lista_actrices:
                    
                    value = True
                    while value == True:
                        try:
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
                
                item.append(producername)
                item.append(self.name)
                try:
                    insert_actress(item)
                except:
                    pass
                movies = get_movies(item[1])
                try:
                    insert_movie(movies,self.name,item[0])
                except:
                    pass
                
                logging.debug('Getting ' + str(item) 
                              + ' : ' + str(q.qsize()) + ' items in queue')
                time.sleep(0.01)
        return

if __name__ == '__main__':
    
    p1 = ProducerThread(name='producer1')
    c1 = ConsumerThread(name='consumer1')
    p2 = ProducerThread(name='producer2')
    c2 = ConsumerThread(name='consumer2')
    p3 = ProducerThread(name='producer3')
    c3 = ConsumerThread(name='consumer3')
    p4 = ProducerThread(name='producer4')
    c4 = ConsumerThread(name='consumer4')

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
































# import threading
# import time
# import logging

# from multiprocessing import Queue
# from scrapping import get_actresses,get_movies



# logging.basicConfig(level=logging.DEBUG,
#                     format='(%(threadName)-9s) %(message)s',)

# BUF_SIZE = 20
# q = Queue(BUF_SIZE)
# list_of_used = []
# class ProducerThread(threading.Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, verbose=None): 
#         super(ProducerThread,self).__init__()
#         self.target = target
#         self.name = name
#         self.lista_actrices = get_actresses('https://en.wikipedia.org/wiki/List_of_American_film_actresses')
#     def run(self):
#         while True:
#             if not q.full():
#                 if self.lista_actrices:
#                     # item = random.choice(self.lista_actrices)
#                     value = True
#                     while value == True:
#                         try:
#                             item = self.lista_actrices[0]
#                             self.lista_actrices.remove(item)
#                             if item not in list_of_used:
#                                 list_of_used.append(item)
#                                 value = False
#                         except:
#                             pass

#                     # item = self.lista_actrices[0]
#                     # self.lista_actrices.remove(item)
#                     q.put(item)
                    
#                     logging.debug('Putting ' + str(item)  
#                                 + ' : ' + str(q.qsize()) + ' items in queue')
#                     time.sleep(0.01)
#         return

# class ConsumerThread(threading.Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, verbose=None):
#         super(ConsumerThread,self).__init__()
#         self.target = target
#         self.name = name
#         return

#     def run(self):
#         while True:
#             if not q.empty():
#                 item = q.get()
#                 # movies = get_movies(item[1])
#                 logging.debug('Getting ' + str(item) 
#                               + ' : ' + str(q.qsize()) + ' items in queue')
#                 time.sleep(0.01)
#         return

# if __name__ == '__main__':
    
#     p1 = ProducerThread(name='producer1')
#     c1 = ConsumerThread(name='consumer1')
#     p2 = ProducerThread(name='producer2')
#     c2 = ConsumerThread(name='consumer2')
#     p3 = ProducerThread(name='producer3')
#     c3 = ConsumerThread(name='consumer3')
#     p4 = ProducerThread(name='producer4')
#     c4 = ConsumerThread(name='consumer4')

#     c1.start()
#     c2.start()
#     c3.start()
#     c4.start()
#     # time.sleep(2)
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     # time.sleep(10)