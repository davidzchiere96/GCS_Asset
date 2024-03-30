from cloudStorageClient import StorageClient
import getStorageBucket
from manageStorageBucket import Bucket
import logger


log = logger.logger()

def input_request():
    operation_number = int(input("Hello! Please, select the operation you want to execute: \n"
                                 " 1 - CREATE A BUCKET\n "
                                 "2 - RETURN AN EXISTENT BUCKET \n "
                                 "\n "))
    return operation_number

def main():
    # service_account_path = r"config\smooth-tesla-413121-a1ac05929582.json"
    # service_account_path = input("Input the service account json path:")
    # storage_client = cloudStorageClient.StorageClient(service_account_path)
    storage_client = StorageClient()
    client = storage_client.get_client()
    log.info("Client connected!")


    operation_required = input_request()
    if operation_required == 1:
        # create_bucket = manageStorageBucket.create_bucket("asset_storage_bucket_stg_newest")
        bucket = Bucket()
        # bucket.create_bucket("asset_storage_bucket_stg_newestest")
        bucket.create_bucket(str(input("Name your gcs-bucket: ")))
    elif operation_required == 2:
        bucket = getStorageBucket.get_bucket("asset_storage_bucket")
    else:
        return 0

    # bucket = getStorageBucket.get_bucket("asset_storage_bucket")
    # create_bucket = manageStorageBucket.create_bucket("asset_storage_bucket_stg")

if __name__ == "__main__":
    main()