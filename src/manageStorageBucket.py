# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logger
from cloudClient import CloudStorageClient
from getStorageObject import BucketGetter


log = logger.logger()

class Bucket:
    def __init__(self):
        self.__storage_client = CloudStorageClient().get_client()
        self.__bucket_getter = BucketGetter()

    """
    def get_bucket(self, bucket_name):
        bucket = self.__bucket_getter.get_bucket(bucket_name)
        log.info(f"Bucket '{bucket_name}' returned!")
        return bucket
    """

    def create_bucket(self, bucket_name):
        new_bucket = self.__storage_client.create_bucket(bucket_name)
        log.info(f"New bucket '{bucket_name}' created!")

    def delete_bucket(self, bucket_name):
        bucket = self.__bucket_getter.get_bucket(bucket_name)
        bucket.delete(force=True)
        log.info(f"Bucket '{bucket_name}' deleted!")


# bucket_manager = Bucket()
# bucket_manager.create_bucket("asset_storage_bucket_april")
# bucket_manager.delete_bucket("asset_storage_bucket_april")
