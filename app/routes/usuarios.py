# app/routes/usuarios.py
from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario, db
from app.models.perfil import Perfil  # Asegúrate de importar esto

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.route("/usuarios/", methods=['GET'])
def get_all():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuarios_bp.route("/usuarios/<id>", methods=['GET'])
def get(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.to_dict())


@usuarios_bp.route("/usuarios/", methods=['POST'])
def create():
    try:
        data = request.get_json()

        # Verificar campos requeridos
        campos_requeridos = ['nombre', 'email', 'password']
        if not all([campo in data for campo in campos_requeridos]):
            return jsonify({"error": "Faltan campos requeridos"}), 400

        # Verificar si el email ya existe
        if Usuario.query.filter_by(email=data['email']).first():
            return jsonify({"error": "Ya existe un usuario con ese email"}), 409

        # Crear usuario
        usuario = Usuario(
            nombre=data['nombre'],
            email=data['email'],
            password=data['password']
        )

        # Crear perfil si viene
        if 'perfil' in data:
            perfil = Perfil(
                rol=data['perfil'].get('rol'),
                estado_rostro=data['perfil'].get('estado_rostro'),
                telefono=data['perfil'].get('telefono'),
                usuario=usuario  # Asocia el perfil al usuario
            )
            db.session.add(perfil)

        db.session.add(usuario)
        db.session.commit()
        return jsonify(usuario.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@usuarios_bp.route("/usuarios/<id>", methods=['PUT'])
def update(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()
    usuario.nombre = data['nombre']
    usuario.email = data['email']
    usuario.password = data['password']

    # Si también deseas actualizar el perfil:
    if 'perfil' in data:
        if usuario.perfil:
            usuario.perfil.rol = data['perfil'].get('rol')
            usuario.perfil.estado_rostro = data['perfil'].get('estado_rostro')
            usuario.perfil.telefono = data['perfil'].get('telefono')
        else:
            # Si no existe el perfil, lo creamos
            from app.models.perfil import Perfil
            perfil = Perfil(
                rol=data['perfil'].get('rol'),
                estado_rostro=data['perfil'].get('estado_rostro'),
                telefono=data['perfil'].get('telefono'),
                usuario=usuario
            )
            db.session.add(perfil)

    db.session.commit()
    return jsonify(usuario.to_dict())



@usuarios_bp.route("/usuarios/<id>", methods=['DELETE'])
def delete(id):
    usuario = Usuario.query.get(id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict())
