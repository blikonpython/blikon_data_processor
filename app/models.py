import logging

from flask import current_app

class FirebaseModel:
    def __init__(self):
        pass
    def get_data(self, path):
        with current_app.app_context():
            db = current_app.config['db']
            data = db.child(path).get().val()
            logging.info(f"Data obtained from Firebase at path '{path}': {data}")
            return data
