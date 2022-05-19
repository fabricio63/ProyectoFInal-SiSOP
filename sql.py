from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model
from sqlalchemy import insert

db = SqliteDatabase('movies.db')

class actrices(Model):
    id_actriz = AutoField()
    name = CharField(unique=True)
    url = CharField()
    idconsumidor = CharField()
    idproductor = CharField()
    

    class Meta:
        database = db

class peliculas(Model):
   film_id = AutoField()
   movie_name = CharField(unique=True)
   url = CharField()
   idconsumidor = CharField()
   
   

   class Meta:
       database = db

class ActricesyPeliculas(Model):
    total_id = AutoField()
    actriz_id = CharField()
    film_id = CharField()
    id_consumidor = CharField()
   

    class Meta:
        database = db

db.connect()
db.create_tables([actrices, peliculas,ActricesyPeliculas])


def insert_actress(item):
    chamo = actrices( name=item[0],
                   url=item[1],
                   idconsumidor=item[3],
                   idproductor=item[2])
    chamo.save()
def insert_actricesypeliculas(actriz,nombrepelicula,consumidor):       
    chamo2 = ActricesyPeliculas(
        actriz_id = actriz,
     film_id = nombrepelicula,
    id_consumidor = consumidor
    )
    chamo2.save()

def insert_movie(movies,consumidor,nombre):

    for i in movies:
        try:
            insert_actricesypeliculas(nombre,i[0],consumidor)
            chamo = peliculas( movie_name=i[0],
                    url=i[1],
                    idconsumidor=consumidor)
            
            chamo.save()
        except:
            insert_actricesypeliculas(nombre,i[0],consumidor)
            
        
        



item = ['kate','wiki','prod1','prod2']

# query = actrices.select()
# print(query.delete_instance())
# try:
#     insert_actress(item)
# except:
#     pass
# for actriz in actrices:
#     print(actriz.idproductor)
# movies=[['21 jump','wiki'],[]]

# # insert_movie(movies,'prod1')
# for movie in peliculas:
#     print(movie.movie_name)