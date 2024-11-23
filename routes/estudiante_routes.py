# routes/estudiante_routes.py
from flask import Blueprint, jsonify, request
from models.estudiante_model import Estudiante
from config import db

estudiante_bp = Blueprint('estudiante_bp', __name__)

@estudiante_bp.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    estudiantes = Estudiante.query.all()
    return jsonify([estudiante.to_dict() for estudiante in estudiantes])

@estudiante_bp.route('/estudiantes', methods=['POST'])
def create_estudiante():
    data = request.get_json()
    nuevo_estudiante = Estudiante(nombre=data['nombre'], correo=data['correo'])
    db.session.add(nuevo_estudiante)
    db.session.commit()
    return jsonify(nuevo_estudiante.to_dict()), 201

@estudiante_bp.route('/estudiantes/<int:id>', methods=['PUT'])
def update_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    data = request.get_json()
    estudiante.nombre = data['nombre']
    estudiante.correo = data['correo']
    #estudiante.curso_id = data.get('curso_id')
    db.session.commit()
    return jsonify(estudiante.to_dict())

@estudiante_bp.route('/estudiantes/<int:id>', methods=['DELETE'])
def delete_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return jsonify({'mensaje': 'Estudiante eliminado correctamente'})