# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Client connector
# Per i log utilizzare nuove librerie assettizzate

import logger
from google.cloud import storage
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"config\smooth-tesla-413121-a1ac05929582.json"
log = logger.logger()

class StorageClient:
    def __init__(self): # , service_account_path=None):
        # self.key_path = service_account_path
        self.client = None

    def connect(self):
        try:
            # self.client = storage.Client.from_service_account_json(json_credentials_path=self.key_path)
            self.client = storage.Client()
            # log.info("Client connected!")
        except Exception as e:
            log.error(f"Error connecting to storage client: {e}")

    def get_client(self):
        if not self.client:
            self.connect()
        return self.client


# Esempio di utilizzo della classe StorageClient
# if __name__ == "__main__":
#    service_account_path = r"config\smooth-tesla-413121-a1ac05929582.json"
#    storage_client = StorageClient(service_account_path)
#    client = storage_client.get_client()










