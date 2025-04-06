from app.models import db
import uuid

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    perfil = db.relationship('Perfil', uselist=False, back_populates='usuario', cascade="all, delete")

    def __repr__(self):
        return f"<Usuario {self.nombre}>"

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'perfil': self.perfil.to_dict() if self.perfil else None
        }

    



    