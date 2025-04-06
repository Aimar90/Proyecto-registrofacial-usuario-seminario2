from flask import Blueprint, request, jsonify
from app.models import db
from app.models.perfil import Perfil
from app.models.usuario import Usuario

perfil_bp = Blueprint('perfil_bp', __name__)

# Crear y asociar perfil a un usuario
@perfil_bp.route("/usuarios/<usuario_id>/perfil", methods=['POST'])
def crear_perfil(usuario_id):
    data = request.get_json()
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    # Validar si ya tiene perfil
    if usuario.perfil:
        return jsonify({"error": "Este usuario ya tiene un perfil"}), 400

    perfil = Perfil(
        rol=data['rol'],
        estado_rostro=data['estado_rostro'],
        telefono=data.get('telefono'),
        usuario=usuario
    )
    db.session.add(perfil)
    db.session.commit()
    return jsonify(perfil.to_dict()), 201

# Consultar el perfil de un usuario
@perfil_bp.route("/usuarios/<usuario_id>/perfil", methods=['GET'])
def obtener_perfil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario or not usuario.perfil:
        return jsonify({"error": "Perfil no encontrado"}), 404
    return jsonify(usuario.perfil.to_dict())

# Modificar el perfil
@perfil_bp.route("/usuarios/<usuario_id>/perfil", methods=['PUT'])
def modificar_perfil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario or not usuario.perfil:
        return jsonify({"error": "Perfil no encontrado"}), 404
    
    data = request.get_json()
    perfil = usuario.perfil
    perfil.rol = data.get('rol', perfil.rol)
    perfil.estado_rostro = data.get('estado_rostro', perfil.estado_rostro)
    perfil.telefono = data.get('telefono', perfil.telefono)
    db.session.commit()
    return jsonify(perfil.to_dict())

# Eliminar perfil
@perfil_bp.route("/usuarios/<usuario_id>/perfil", methods=['DELETE'])
def eliminar_perfil(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario or not usuario.perfil:
        return jsonify({"error": "Perfil no encontrado"}), 404

    db.session.delete(usuario.perfil)
    db.session.commit()
    return jsonify({"mensaje": "Perfil eliminado correctamente"})

