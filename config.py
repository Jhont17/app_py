from flask_sqlalchemy import  SQLAlchemy

#variables para la configuracion
DB_USERNAME = 'admin'
DB_PASSWORD = 'admin'
DB_HOST = 'localhost'
DB_NAME = 'gestion_estudiantes'

#configuracion de la base de datos
DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
db = SQLAlchemy()