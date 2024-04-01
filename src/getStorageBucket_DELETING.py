# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Bucket connector

import logger
# import cloudStorageClient
from cloudStorageClient import StorageClient

log = logger.logger()

# def get_bucket():
def get_bucket(gcs_bucket):
    storage_client = StorageClient()
    client = storage_client.get_client()
    # bucket_name = "asset_storage_bucket"
    bucket_name = gcs_bucket
    # USE THIS:
    # bucket_name = input(f"Bucket name: ")
    bucket = client.get_bucket(bucket_name)
    log.info(f"Bucket {bucket_name} returned!")

    return bucket

# get_bucket("asset_storage_bucket")