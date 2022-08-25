from werkzeug.security import check_password_hash, generate_password_hash
#is active
from flask_login import UserMixin


class Resultado1(UserMixin):

    def __init__(self, id, q1, q2, q3, q4, usuarios_id) -> None: 
        self.id = id
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.usuarios_id = usuarios_id