from .entities.Perfil import Perfil

class ModelPerfil():

    @classmethod
    def register(self, db, perfil):
        try:
            cur = db.connection.cursor()
            cur.execute("INSERT INTO perfiles (curso, carrera, habilidad, universidad) VALUES (%s, %s, %s, %s)",(perfil.curso,perfil.carrera,perfil.habilidad,perfil.universidad))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def read(self, db):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM perfiles")
            data_perfil = cur.fetchall()
            cur.close()
            return data_perfil
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete(self, db, id):
        try:
            cursor=db.connection.cursor()
            cursor.execute("DELETE FROM perfiles WHERE id=%s", (id))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def update(self, db,curso,carrera,habilidad,universidad, id):
        try:
            cur = db.connection.cursor()
            cur.execute ("UPDATE perfiles SET curso=%s, carrera=%s, habilidad=%s, universidad=%s WHERE id=%s " , (curso, carrera, habilidad, universidad, id))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)