# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Client connector

import logging
import os
from google.cloud import storage


logging.getLogger().setLevel(logging.INFO)

def storage_client():
    # service account key JSON path
    key_path = r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\GCS_Asset\GCS_Asset\src\config\smooth-tesla-413121-a1ac05929582.json"

    # cs = storage.Client()
    # client = cs.from_service_account_json(key_path)
    client = storage.Client.from_service_account_json(json_credentials_path=key_path)
    logging.info("client connected")

    return client


storage_client()










