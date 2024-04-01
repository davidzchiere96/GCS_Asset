from manageStorageBucket import Bucket
from manageStorageFile import File
import logger
import inputRequests


log = logger.logger()

def manage_bucket():
    operation_required = inputRequests.input_operation_request_for_bucket()

    if operation_required == 1:
        bucket = Bucket()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket.create_bucket(bucket_name)

    elif operation_required == 2:
        bucket = Bucket()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket.delete_bucket(bucket_name)

    elif operation_required == 3:
        bucket = Bucket()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket.get_bucket(bucket_name)

    else:
        log.info("No operation found!")
        return

def manage_file():
    operation_required = inputRequests.input_operation_request_for_file()

    if operation_required == 1:
        file = File()
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file_path = inputRequests.input_source_file_path()
        file.upload_file(bucket_name, file_name, file_path)

    elif operation_required == 2:
        file = File()
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file_path = inputRequests.input_source_file_path()
        file.download_file(bucket_name, file_name, file_path)

    elif operation_required == 3:
        file = File()
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        file.delete_file(bucket_name, file_name)

    else:
        log.info("No operation found!")
        return


def main():

    # operation_required = inputRequests.input_operation_request()
    operation_required = inputRequests.input_operation_request_domain()

    if operation_required == 1:
        manage_bucket()

    elif operation_required == 2:
        manage_file()

    else:
        log.info("No object found!")
        return

if __name__ == "__main__":
    main()