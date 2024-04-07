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
        file_size = self.__file.get_local_file_size(local_file_path)

        if file_size > 1.0:
            # MANCA PROCEDURA DI GRACEFUL SHUTDOWN
            """Upload a large file to GCS using streaming"""
            with open(local_file_path, "rb") as f:
                blob.upload_from_file(f)

            log.info(f"streaming...")
            log.info(f"File '{local_file_path}' uploaded to '{bucket_name}/{file_name}'")
            return

        else:
            file_to_upload = blob.upload_from_filename(local_file_path)
            log.info(f"File '{local_file_path}' uploaded to '{bucket_name}/{file_name}'")

        return

    def download_file(self, bucket_name, file_name, destination_path):
        bucket = self.__bucket.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        file_size = self.__file.get_file_size(bucket_name, file_name)

        if file_size > 1:
            # MANCA PROCEDURA DI GRACEFUL SHUTDOWN
            """Download a large file from GCS using streaming"""
            with open(destination_path, "wb") as f:
                blob.download_to_file(f)

            log.info(f"streaming...")
            log.info(f"File '{bucket_name}/{file_name}' downloaded to '{destination_path}'")
            return

        else:
            file_to_download = blob.download_to_filename(destination_path)
            log.info(f"File '{file_name}' downloaded from bucket '{bucket_name}' to '{destination_path}'.")

        return

    def delete_file(self, bucket_name, file_name):
        bucket = self.__bucket.get_bucket(bucket_name)

        blob = bucket.blob(file_name)

        file_to_delete = blob.delete()
        log.info(f"File '{file_name}' deleted from bucket '{bucket_name}'.")
        return

    def write_to_file(self, bucket_name, file_name, message):
        try:
            """Write and read a blob from GCS using file-like IO"""
            bucket = self.__bucket.get_bucket(bucket_name)

            blob = bucket.blob(file_name)

            with blob.open("w") as f:
                f.write(message)
                log.info(f"Message written in file '{file_name}'")

        except FileNotFoundError:
            log.info("File not found.")

    def read_from_file(self, bucket_name, file_name):
        try:
            """Write and read a blob from GCS using file-like IO"""
            bucket = self.__bucket.get_bucket(bucket_name)

            blob = bucket.blob(file_name)

            with blob.open("r") as f:
                log.info(f"Read file '{file_name}'")
                print(f.read())

        except FileNotFoundError:
            log.info("File not found.")

    def update_file_storage_class(self, bucket_name, file_name, storage_class):
        bucket = self.__bucket.get_bucket(bucket_name)
        blob = bucket.blob(file_name)

        blob.update_storage_class(storage_class)  # es. "NEARLINE"
        log.info(f"Storage class of the object '{file_name}' updated to '{storage_class}'")
        return

# file = File()
# file.upload_file("asset_storage_bucket", "message_streaming.json", "config\message.json")
# file.download_file("asset_storage_bucket", "message_streaming.json", "config\message_streaming.json")

    # MUOVI UN FILE DA UN BUCKET AD UN ALTRO
    # CREA UNA DIRECTORY NEL BUCKET
    # ELIMINA UNA DIRECTORY NEL BUCKET

# file = File()
# file.download_file("asset_storage_bucket", "april_fool.json", "config\message_april_fool.json")
# file.delete_file("asset_storage_bucket", "april_fool.json")


# File().delete_file("asset_storage_bucket", "message_new_incapsulated.json")
# download_file("asset_storage_bucket", "message_newest.json", "config\message_newest.json")
# delete_file("asset_storage_bucket", "message_newest.json")

