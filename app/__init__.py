from flask import Flask
from .config import Config
import pyrebase
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    firebase = pyrebase.initialize_app(app.config['FIREBASE_CONFIG'])
    app.config['db'] = firebase.database()

    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app