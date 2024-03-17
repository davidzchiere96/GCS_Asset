# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
import logging

import cloudStorage
import getStorageBucket
# from google.cloud import storage

client = cloudStorage.storage_client()


def create_new_bucket():

    # new_bucket_name = input(f"Bucket to create: ")

    new_bucket_name = "asset_storage_bucket_new"
    new_bucket = client.create_bucket(new_bucket_name)

    logging.info(f"New bucket {new_bucket_name} created!")
    return new_bucket


def delete_bucket():

    # bucket_name = "asset_storage_bucket_new"
    # bucket = client.get_bucket(bucket_name)

    bucket = getStorageBucket.get_bucket_name()

    bucket.delete(force=True)

    logging.info("Bucket deleted!")
    return bucket

# create_new_bucket()
# delete_bucket()