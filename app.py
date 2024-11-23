# app.py
from flask import Flask, jsonify
from config import db, DATABASE_URI
from routes.estudiante_routes import estudiante_bp
#from routes.curso_routes import curso_bp
#from routes.profesor_routes import profesor_bp
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)

# Configurar CORS globalmente para todas las rutas
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar las rutas
app.register_blueprint(estudiante_bp, url_prefix='/api/v1.0')
#app.register_blueprint(curso_bp, url_prefix='/api/v1.0')
#app.register_blueprint(profesor_bp, url_prefix='/api/v1.0')

# Crear las tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)