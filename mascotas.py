from database import db
from sqlalchemy.sql import func

class Mascota(db.Model):
    
    __tablename__ = 'mascotas'
         
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    duenio = db.Column(db.String(100))
    
    def __init__(self, nombre, especie, raza, duenio):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.duenio = duenio

    def __repr__(self):
        return f'<Mascota {self.id}>: {self.nombre}, {self.especie}, {self.raza}, {self.duenio}'
