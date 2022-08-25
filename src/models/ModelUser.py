from .entities.User import User
from werkzeug.security import check_password_hash, generate_password_hash

class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, username, password, fullname, tipo FROM usuarios WHERE username = '{}'".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3],row[4])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor=db.connection.cursor()
            sql="SELECT id, username, fullname, tipo FROM usuarios WHERE id = {}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                logged_user=User(row[0],row[1],None,row[2])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def register_user(self, db, user):
        try:
            user.password=generate_password_hash(user.password)
            cur = db.connection.cursor()
            cur.execute("INSERT INTO usuarios (username, password, fullname, tipo) VALUES (%s, %s, %s, %s)",(user.username,user.password,user.fullname,user.tipo))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
        
