from google.cloud import firestore
import logging
import os

class FirebaseModel:
    def __init__(self):
        self.db = firestore.Client(project='gforcereportes')  # Asegúrate de especificar el proyecto correcto

    def get_data(self, field):
        try:
            doc_ref = self.db.collection('blikon').document('general')
            doc = doc_ref.get()
            if doc.exists:
                data = doc.to_dict().get(field)
                if data is None:
                    logging.warning(f"No data found for field '{field}' in document 'general'")
                else:
                    logging.info(f"Data obtained from Firestore for field '{field}': {data}")
                return data
            else:
                logging.warning(f"Document 'general' does not exist")
                return None
        except Exception as e:
            logging.error(f"Error accessing data for field '{field}' in document 'general': {e}")
            return None
