# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Client connector
# Per i log utilizzare nuove librerie assettizzate

#import logging
import logger
from google.cloud import storage


log = logger.logger()

# logging.getLogger().setLevel(logging.INFO)

def storage_client():      # def storage_client(service_account_path):
    # service account key JSON path
    key_path = r"config\smooth-tesla-413121-a1ac05929582.json"    # key_path = service_account_path
    # absolute path: C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\GCS_Asset\GCS_Asset\src\config\smooth-tesla-413121-a1ac05929582.json"

    # cs = storage.Client()
    # client = cs.from_service_account_json(key_path)
    client = storage.Client.from_service_account_json(json_credentials_path=key_path)
    log.info("Client connected")

    return client


storage_client()










