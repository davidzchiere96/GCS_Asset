# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logging
import cloudStorage
from google.cloud import storage


# Imposta il percorso del tuo file JSON di chiave di servizio
key_path = r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\GCS_Asset\GCS_Asset\src\config\smooth-tesla-413121-a1ac05929582.json"

# Crea un client di storage
#cs = storage.Client()
#client = cs.from_service_account_json(key_path)
client_storage = storage.Client.from_service_account_json(key_path)


# Sostituisci "il_tuo_bucket" con il nome del tuo bucket
bucket_name = "asset_storage_bucket"
#logging.info("ok bucket name")
#print("ok")
bucket = client_storage.get_bucket(bucket_name)

# Esempio di upload di un file
#blob = bucket.blob("message_new.json")
#blob.upload_from_filename(r"C:\Users\ECHIERDF9\PycharmProjects\GCS_Asset_pythonProject\gcs_asset\message.json")









#
# cs = storage.Client()
#
#
# def get_content(remote_filename):
#     """Download remote file"""
#     paths = remote_filename.split('/')
#     bucket_name = paths[0]
#     filename = '/'.join(paths[1:])
#     data = cs.get_bucket(bucket_name).blob(filename).download_as_string()
#     return data.decode('utf-8')
#
#
# def get_bucket_from_filename(filename):
#     """Get configurations"""
#     return filename.split('/')[0]
