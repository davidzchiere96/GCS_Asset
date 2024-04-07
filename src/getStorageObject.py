import os
import logger
from cloudClient import CloudStorageClient


log = logger.logger()

class BucketGetter:
    def __init__(self):
        self.__storage_client = CloudStorageClient().get_client()

    def get_bucket(self, bucket_name):
        bucket = self.__storage_client.get_bucket(bucket_name)
        log.info(f"Bucket '{bucket_name}' returned!")
        return bucket

class FileGetter:
    def __init__(self):
        self.__bucket = BucketGetter()

    def get_file(self, bucket_name, file_name):
        bucket = self.__bucket.get_bucket(bucket_name)
        blob = bucket.blob(file_name)
        log.info(f"File '{file_name}' from buket '{bucket_name}' returned!")

    def get_file_size(self, bucket_name, file_name):
        """Get the size of a GCS file."""
        bucket = self.__bucket.get_bucket(bucket_name)
        blob = bucket.blob(file_name)

        size_in_bytes = float(blob.size)
        size_in_kb = size_in_bytes/1024
        size_in_mb = size_in_kb/1024
        size_in_gb = size_in_mb/1024

        log.info(f"File '{file_name}' size is: '{size_in_gb}'GB")
        return size_in_gb

    def get_local_file_size(self, file_path):
        """Get the size of a local file."""
        # Check if the file exists
        if os.path.exists(file_path):
            # Get the size of the file
            size_in_bytes = float(os.path.getsize(file_path))
            size_in_kb = size_in_bytes/1024
            size_in_mb = size_in_kb/1024
            size_in_gb = size_in_mb/1024

            log.info(f"File '{file_path}' size is: '{size_in_gb}'GB")
            return size_in_gb
        else:
            return None

# file = FileGetter()
# file.get_file_size("asset_storage_bucket", "message.json")
# file.get_local_file_size("config/message.json")

# bucket = BucketGetter()
# bucket.get_bucket("asset_storage_bucket")

# file = FileGetter()
# file.get_file("asset_storage_bucket","message.json")
