from components.gcp_lib.cloud_storage.storageBucketManager import Bucket, manage_bucket
from components.gcp_lib.cloud_storage.storageFileManager import File, manage_file
from components.gcp_lib.cloud_storage.storageGetter import FileGetter, BucketGetter
from components.logger import Log
import components.inputRequests as inputRequests


log_instance = Log()
log = log_instance.logger()

def get_infos(info_required):

    # Get file size
    if info_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_prefix = inputRequests.input_file_prefix()
        FileGetter(bucket_name).list_files(file_prefix)

    # List of files within a bucket
    elif info_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        file_name = inputRequests.input_destination_file_name()
        # file_path = inputRequests.input_source_file_path()
        FileGetter(bucket_name, file_name).get_file_size()

    else:
        log.warning("No info retrieved!")
        return

def manage_objects(operation_required):

    # Manage bucket
    if operation_required == 1:
        manage_bucket()

    # Manage blob
    elif operation_required == 2:
        manage_file()

    else:
        log.warning("No object found!")
        return


def main():

    domain_required = inputRequests.input_domain()
    if domain_required == 1:
        info_required = inputRequests.input_to_get_info()
        get_infos(info_required)
    elif domain_required == 2:
        operation_required = inputRequests.input_operation()
        manage_objects(operation_required)
    else:
        log.warning("No request domain found!")
        return


if __name__ == "__main__":
    main()