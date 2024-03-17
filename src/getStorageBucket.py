# https://googleapis.github.io/google-cloud-python/latest/storage/index.html
import logging

import cloudStorage
# from google.cloud import storage

client = cloudStorage.storage_client()

def get_bucket_name():
    bucket_name = "asset_storage_bucket"
    # USE THIS:
    # bucket_name = input(f"Bucket name: ")
    bucket = client.get_bucket(bucket_name)

    return(bucket)

# get_bucket_name()