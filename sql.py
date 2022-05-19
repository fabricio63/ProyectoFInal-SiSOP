from peewee import SqliteDatabase, AutoField, CharField, DateField, ForeignKeyField, Model
from sqlalchemy import insert
#creacion de la base de datos en blanco
db = SqliteDatabase('movies.db')
#definicion de clase actrices para la base de datos
class actrices(Model):
    id_actriz = AutoField()
    #restriccion a que sean campos unicos por medio del nombre de la actriz
    name = CharField(unique=True)
    url = CharField()
    idconsumidor = CharField()
    idproductor = CharField()
    

    class Meta:
        database = db
#definicion de clase peliculas para la base de datos
class peliculas(Model):
    #restriccion a que sean campos unicos por medio del nombre de la pelicula
   film_id = AutoField()
   movie_name = CharField(unique=True)
   url = CharField()
   idconsumidor = CharField()
   
   

   class Meta:
       database = db
#definicion de clase de relacion entre peliculas y actrices para la base de datos
class ActricesyPeliculas(Model):
    
    total_id = AutoField()
    actriz_id = CharField()
    film_id = CharField()
    id_consumidor = CharField()
   

    class Meta:
        database = db

db.connect()
#creacion de las tablas en la base de datos
db.create_tables([actrices, peliculas,ActricesyPeliculas])

#funcion de insert de instancias a la db
def insert_actress(item):
    chamo = actrices( name=item[0],
                   url=item[1],
                   idconsumidor=item[3],
                   idproductor=item[2])
    chamo.save()

#funcion de insert de instancias a la db
def insert_actricesypeliculas(actriz,nombrepelicula,consumidor):       
    chamo2 = ActricesyPeliculas(
        actriz_id = actriz,
     film_id = nombrepelicula,
    id_consumidor = consumidor
    )
    chamo2.save()
#funcion de insert de instancias a la db hace un for sobre listado de peliculas de la actriz y tambien el for para la relacion de la tabla de fact
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
            
        
        





