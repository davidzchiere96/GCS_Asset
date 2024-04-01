# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logger
from manageStorageBucket import Bucket
from getStorageObject import BucketGetter, FileGetter

# Per implementare procedura di graceful shutdown
# import os
# import signal
# from contextlib import contextmanager


log = logger.logger()

class File:
    def __init__(self):
         self.__file = FileGetter()
         self.__bucket = BucketGetter()

    def upload_file(self, bucket_name, file_name, local_file_path):
        bucket = self.__bucket.get_bucket(bucket_name)

        blob = bucket.blob(file_name)
        file_to_upload = blob.upload_from_filename(local_file_path)
        log.info(f"File '{file_name}' uploaded in bucket '{bucket_name}'.")
        return


    def download_file(self, bucket_name, file_name, destination_path):
        bucket = self.__bucket.get_bucket(bucket_name)

        blob = bucket.blob(file_name)
        file_to_download = blob.download_to_filename(destination_path)
        log.info(f"File '{file_name}' downloaded from bucket '{bucket_name}' to '{destination_path}'.")
        return

    def delete_file(self, bucket_name, file_name):
        bucket = self.__bucket.get_bucket(bucket_name)

        blob = bucket.blob(file_name)

        file_to_delete = blob.delete()
        log.info(f"File '{file_name}' deleted from bucket '{bucket_name}'.")
        return

    # MUOVI UN FILE DA UN BUCKET AD UN ALTRO
    # CREA UNA DIRECTORY NEL BUCKET
    # ELIMINA UNA DIRECTORY NEL BUCKET

# file = File()
# file.download_file("asset_storage_bucket", "april_fool.json", "config\message_april_fool.json")
# file.delete_file("asset_storage_bucket", "april_fool.json")


# File().delete_file("asset_storage_bucket", "message_new_incapsulated.json")
# download_file("asset_storage_bucket", "message_newest.json", "config\message_newest.json")
# delete_file("asset_storage_bucket", "message_newest.json")



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
