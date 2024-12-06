# routes/curso_routes.py

from flask import Blueprint, jsonify, request
from models.curso_model import Curso
from config import db

curso_bp = Blueprint('curso_bp', __name__)

@curso_bp.route('/cursos', methods=['GET'])
def get_cursos():
    cursos = Curso.query.all()
    return jsonify([curso.to_dict() for curso in cursos])

@curso_bp.route('/cursos', methods=['POST'])
def create_curso():
    data = request.get_json()
    nuevo_curso = Curso(nombre=data['nombre'], descripcion=data.get('descripcion'))
    db.session.add(nuevo_curso)
    db.session.commit()
    return jsonify(nuevo_curso.to_dict()), 201

@curso_bp.route('/cursos/<int:id>', methods=['PUT'])
def update_curso(id):
    curso = Curso.query.get_or_404(id)
    data = request.get_json()
    curso.nombre = data['nombre']
    curso.descripcion = data.get('descripcion')
    db.session.commit()
    return jsonify(curso.to_dict())

@curso_bp.route('/cursos/<int:id>', methods=['DELETE'])
def delete_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return jsonify({'mensaje': 'Curso eliminado correctamente'})
