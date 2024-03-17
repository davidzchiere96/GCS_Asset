# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
# Bucket connector

import logger
import cloudStorage

log = logger.logger()
client = cloudStorage.storage_client()

def get_bucket_name():  # def get_bucket_name(gcs_bucket):
    bucket_name = "asset_storage_bucket"  # bucket_name = "asset_storage_bucket"
    # USE THIS:
    # bucket_name = input(f"Bucket name: ")
    bucket = client.get_bucket(bucket_name)
    log.info("Bucket connected")

    return(bucket)

get_bucket_name()