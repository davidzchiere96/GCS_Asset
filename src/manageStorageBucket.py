# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logger
from cloudStorageClient import StorageClient
from getStorageBucket import get_bucket


log = logger.logger()

class Bucket:
    def __init__(self):
        self.storage_client = StorageClient().get_client()

    def create_bucket(self, bucket_name):
        new_bucket = self.storage_client.create_bucket(bucket_name)
        log.info(f"New bucket {bucket_name} created!")

    def delete_bucket(self, bucket_name):
        bucket = get_bucket(bucket_name)
        bucket.delete(force=True)
        log.info(f"Bucket {bucket_name} deleted!")


#    bucket_manager = Bucket()
#    bucket_manager.create_bucket("bucket_due")
#    bucket_manager.delete_bucket("bucket_due")
