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

        if file_size > 1:
            # PROCEDURA DI GRACEFUL SHUTDOWN E UPLOAD STREAMING
            return

        else:
            file_to_upload = blob.upload_from_filename(local_file_path)
            log.info(f"File '{file_name}' uploaded in bucket '{bucket_name}'.")

        return

    def download_file(self, bucket_name, file_name, destination_path):
        bucket = self.__bucket.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        file_size = self.__file.get_file_size(bucket_name, file_name)

        if file_size > 1:
            # PROCEDURA DI GRACEFUL SHUTDOWN E DOWNLOAD STREAMING
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
# file.write_to_file("asset_storage_bucket", "message.json", "    ciao")

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
