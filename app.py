from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from models.user import db, bcrypt
from routes.auth import auth

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
bcrypt.init_app(app)
JWTManager(app)

app.register_blueprint(auth, url_prefix='/api/auth')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)