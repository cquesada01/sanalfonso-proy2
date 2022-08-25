from .entities.Resultado1 import Resultado1

class ModelResultado1():

    @classmethod
    def register(self, db, resultado):
        try:
            cur = db.connection.cursor()
            cur.execute("INSERT INTO prueba1 (q1, q2, q3, q4, usuarios_id) VALUES (%s, %s, %s, %s, %s)",(resultado.q1,resultado.q2,resultado.q3,resultado.q4, resultado.usuarios_id))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)


