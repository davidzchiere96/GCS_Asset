# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logger
import cloudStorageClient
import getStorageBucket

# Per implementare procedura di graceful shutdown
# import os
# import signal
# from contextlib import contextmanager


log = logger.logger()
client = cloudStorageClient.storage_client()


def upload_file(bucket_name, file_name, local_file_path):

    bucket = getStorageBucket.get_bucket(bucket_name)
    # istanzia la creazione dell'oggetto blob
    blob = bucket.blob(file_name)

    # upload del file
    file_to_upload = blob.upload_from_filename(local_file_path)

    log.info(f"File {file_name} uploaded in bucket {bucket_name}.")
    return


def download_file(bucket_name, file_name, destination_path):

    bucket = getStorageBucket.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    # download del file
    file_to_download = blob.download_to_filename(destination_path)

    log.info(f"File {file_name} downloaded from bucket {bucket_name} to {destination_path}.")
    return


def delete_file(bucket_name, file_name):

    bucket = getStorageBucket.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    file_to_delete = blob.delete()

    log.info(f"File {file_name} deleted from bucket {bucket_name}.")
    return


# upload_file("asset_storage_bucket", "message_newest.json", "config\message.json")
# download_file("asset_storage_bucket", "message_newest.json", "config\message_newest.json")
# delete_file("asset_storage_bucket", "message_newest.json")



#    file_name = "asset_storage_file_new"
#    bucket = client.get_bucket(bucket_name)
#    bucket.delete(force=True)

#    logging.info("Bucket deleted!")
#    return bucket



# Sostituisci "il_tuo_bucket" con il nome del tuo bucket
#bucket_name = "asset_storage_bucket"
#logging.info("ok bucket name")
#print("ok")
#bucket = client_storage.get_bucket(bucket_name)

# Esempio di upload di un file
#blob = bucket.blob("message_new.json")
#blob.upload_from_filename(r"C:\Users\ECHIERDF9\PycharmProjects\GCS_Asset_pythonProject\gcs_asset\message.json")




# Sostituisci "il_tuo_bucket" con il nome del tuo bucket
# bucket_name = "asset_storage_bucket"
# logging.info("ok bucket name")
# print("ok")
# bucket = client.get_bucket(bucket_name)

# print(client, bucket)

# Esempio di upload di un file
# blob = bucket.blob("message_new.json")
# blob.upload_from_filename(r"C:\Users\ECHIERDF9\PycharmProjects\GCS_Asset_pythonProject\gcs_asset\message.json")




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
