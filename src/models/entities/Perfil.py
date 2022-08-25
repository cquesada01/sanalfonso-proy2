from werkzeug.security import check_password_hash, generate_password_hash
#is active
from flask_login import UserMixin


class Perfil(UserMixin):

    def __init__(self, id, curso, carrera, habilidad, universidad) -> None: 
        self.id = id
        self.curso = curso
        self.carrera = carrera
        self.habilidad = habilidad
        self.universidad = universidad