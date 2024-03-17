# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
import logging
import cloudStorage
import getStorageBucket
#from google.cloud import storage

client = cloudStorage.storage_client()

bucket = getStorageBucket.get_bucket_name()

def upload_file():

    file_name = "message_new.json"
    # USE THIS:
    # file_name = input(f"File to upload in the bucket {bucket_name}: ")

    # istanzia la creazione dell'oggetto blob
    blob = bucket.blob(file_name)

    local_file_path = r"C:\Users\ECHIERDF9\OneDrive - NTT DATA EMEAL\Desktop\GCS_Asset\GCS_Asset\src\config\message.json"
    # USE THIS:
    # local_file_path = input(f"Local file path: ")

    # upload del file
    file_to_upload = blob.upload_from_filename(local_file_path)

    logging.info(f"File {file_name} uploaded in bucket {bucket}!")
    return file_to_upload


# def download_file():

# def delete_file():




#    file_name = "asset_storage_file_new"
#    bucket = client.get_bucket(bucket_name)
#    bucket.delete(force=True)

#    logging.info("Bucket deleted!")
#    return bucket

#upload_file()
#download_file()
#delete_file()

# Sostituisci "il_tuo_bucket" con il nome del tuo bucket
#bucket_name = "asset_storage_bucket"
#logging.info("ok bucket name")
#print("ok")
#bucket = client_storage.get_bucket(bucket_name)

# Esempio di upload di un file
#blob = bucket.blob("message_new.json")
#blob.upload_from_filename(r"C:\Users\ECHIERDF9\PycharmProjects\GCS_Asset_pythonProject\gcs_asset\message.json")
