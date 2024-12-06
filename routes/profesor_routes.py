# routes/profesor_routes.py
from flask import Blueprint, jsonify, request
from models.profesor_model import Profesor
from config import db

profesor_bp = Blueprint('profesor_bp', __name__)

@profesor_bp.route('/profesores', methods=['GET'])
def get_profesores():
    profesores = Profesor.query.all()
    return jsonify([profesor.to_dict() for profesor in profesores])

@profesor_bp.route('/profesores', methods=['POST'])
def create_profesor():
    data = request.get_json()
    nuevo_profesor = Profesor(nombre=data['nombre'], especialidad=data['especialidad'])
    db.session.add(nuevo_profesor)
    db.session.commit()
    return jsonify(nuevo_profesor.to_dict()), 201

@profesor_bp.route('/profesores/<int:id>', methods=['PUT'])
def update_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    data = request.get_json()
    profesor.nombre = data['nombre']
    profesor.especialidad = data['especialidad']
    db.session.commit()
    return jsonify(profesor.to_dict())


@profesor_bp.route('/profesores/<int:id>', methods=['DELETE'])
def delete_profesor(id):
    profesor = Profesor.query.get_or_404(id)
    db.session.delete(profesor)
    db.session.commit()
    return jsonify({'mensaje': 'Profesor eliminado correctamente'})
