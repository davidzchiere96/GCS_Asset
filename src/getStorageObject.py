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


# bucket = BucketGetter()
# bucket.get_bucket("asset_storage_bucket")

# file = FileGetter()
# file.get_file("asset_storage_bucket","message.json")
