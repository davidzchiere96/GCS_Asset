from cloudStorageClient import StorageClient
import getStorageBucket
from manageStorageBucket import Bucket
from manageStorageFile import File
import logger
import inputRequests


log = logger.logger()

def main():

    operation_required = inputRequests.input_operation_request()

    if operation_required == 1:
        # create_bucket = manageStorageBucket.create_bucket("asset_storage_bucket_stg_newest")
        bucket = Bucket()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket.create_bucket(bucket_name)
    elif operation_required == 2:
        file = File()
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file_path = inputRequests.input_source_file_path()
        file.upload_file(bucket_name, file_name, file_path)

        # file.download_file("asset_storage_bucket", "message_newest.json", "config\message_newest.json")
        # file.delete_file("asset_storage_bucket", "message_newest.json")
    elif operation_required == 3:
        bucket_name = inputRequests.input_destination_bucket_name()
        getStorageBucket.get_bucket(bucket_name)
    else:
        return 0

    # bucket = getStorageBucket.get_bucket("asset_storage_bucket")
    # create_bucket = manageStorageBucket.create_bucket("asset_storage_bucket_stg")

if __name__ == "__main__":
    main()