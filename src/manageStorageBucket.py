# https://googleapis.github.io/google-cloud-python/latest/storage/index.html

import logger
import cloudStorage
import getStorageBucket
# from google.cloud import storage

log = logger.logger()
client = cloudStorage.storage_client()

def create_bucket(bucket_name):

    # new_bucket_name = input(f"Bucket to create: ")

    new_bucket = client.create_bucket(bucket_name)

    log.info(f"New bucket {bucket_name} created!")
    return


def delete_bucket(bucket_name):

    # bucket_name = "asset_storage_bucket_new"
    # bucket = client.get_bucket(bucket_name)

    bucket = getStorageBucket.get_bucket(bucket_name)
    bucket.delete(force=True)

    log.info(f"Bucket {bucket_name} deleted!")
    return

# create_bucket("bucket_due")
# delete_bucket("bucket_due")