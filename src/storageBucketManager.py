from logger import Log
from google.cloud.storage import constants
from cloudClient import CloudStorageClient
from storageGetter import BucketGetter
import inputRequests


log_instance = Log()
log = log_instance.logger()

class Bucket:
    def __init__(self, bucket_name):

        """API connectors"""""""""""""""""""""""""""""""""""""""""""""
        self.__storage_client = CloudStorageClient().get_client()
        self.__bucket_getter = BucketGetter(bucket_name)
        self.__declare_bucket = self.__bucket_getter.declare_bucket()
        self.__get_bucket = self.__bucket_getter.get_bucket()
        self.input_bucket_name = bucket_name

        """Bucket Metadata"""""""""""""""""""""""""""""""""""""""""""""
        self.id = self.__declare_bucket.id
        self.name = self.__declare_bucket.name
        self.storage_class = self.__declare_bucket.storage_class
        self.location = self.__declare_bucket.location
        self.location_type = self.__declare_bucket.location_type
        self.lifecycle_rules = self.__declare_bucket.lifecycle_rules
        self.time_created = self.__declare_bucket.time_created
        self.versioning = self.__declare_bucket.versioning_enabled
        self.labels = self.__declare_bucket.labels
        self.retention_period = self.__declare_bucket.retention_period
        self.object_retention_mode = self.__declare_bucket.object_retention_mode

        # self.retention_policy_effective_time
        # self.retention_policy_locked
        # self.cors = self.__declare_bucket.cors
        # self.default_event_based_hold = self.__declare_bucket.default_event_based_hold
        # print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
        # print(f"Metageneration: {bucket.metageneration}")
        # print(
        #     f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
        # )
        # print(f"Requester Pays: {bucket.requester_pays}")
        # print(f"Self Link: {bucket.self_link}")


    def create_bucket(self, local_zone="eu", storage_class="Standard"):
        # self.location = local_zone
        # self.storage_class = storage_class
        new_bucket = self.__storage_client.create_bucket(self.input_bucket_name, location=local_zone)
        # self.storage_class = storage_class
        log.info(
            f"New bucket '{self.input_bucket_name}' created in local zone '{local_zone}' "
            f"with storage class '{storage_class}'"
        )
        return

    def delete_bucket(self,force=True):
        # bucket = self.__bucket_getter.get_bucket()
        bucket = self.__get_bucket
        bucket.delete(force=force)
        log.info(f"Bucket '{self.name}' deleted!")
        return

    def print_bucket_metadata(self):
        metadata = {
            'id': self.id,
            'name': self.name,
            'storage_class': self.storage_class,
            'location': self.location,
            'location_type': self.location_type,
            'lifecycle_rules': self.lifecycle_rules,
            'time_created': self.time_created,
            'versioning': self.versioning,
            'labels': self.labels,
            'retention_period': self.retention_period,
            'object_retention_mode': self.object_retention_mode,
        }
        log.info(f"Bucket {self.name} metadata: {metadata}")
        return

    """Deprecated"""
    # def update_bucket_location(self, local_zone="eu"):
    #    bucket = self.__get_bucket
    #    bucket.location = local_zone
    #    log.info(f"Location for bucket '{self.name}' has been set to '{local_zone}'.")

    def update_bucket_storage_class(self, storage_class="Standard"):
        bucket = self.__get_bucket
        bucket.storage_class = storage_class   # constants.COLDLINE_STORAGE_CLASS
        bucket.patch()
        log.info(f"Default storage class for bucket '{self.name}' has been set to '{bucket.storage_class}'.")
        return



# bucket = Bucket("bucket_chieregatod_gcs_asset")
# bucket.print_bucket_metadata()
# bucket.delete_bucket()
# bucket = Bucket("bucket_chieregatod_test")
# bucket.update_bucket_location()
# bucket.create_bucket(storage_class="NEARLINE")
# bucket=bucket.create_bucket("europe-west8")

    # TODO: controllo versioni degli oggetti

    # TODO: def lifecycle_management
    # def enable_bucket_lifecycle_management(self):
    #     # bucket_name = "my-bucket"
    #     bucket = self.__get_bucket
    #     lifecycle_rules = bucket.lifecycle_rules
    #
    #     print(f"Lifecycle management rules for bucket {self.name} are {list(lifecycle_rules)}")
    #     bucket.add_lifecycle_delete_rule(age=2)
    #     bucket.patch()
    #
    #     lifecycle_rules = bucket.lifecycle_rules
    #     print(f"Lifecycle management is enable for bucket {self.name} and the rules are {list(lifecycle_rules)}")
    #
    #     return bucket
    #
    # def disable_bucket_lifecycle_management(bucket_name):
    #     """Disable lifecycle management for a bucket"""
    #     # bucket_name = "my-bucket"
    #
    #     storage_client = storage.Client()
    #
    #     bucket = storage_client.get_bucket(bucket_name)
    #     bucket.clear_lifecyle_rules()
    #     bucket.patch()
    #     rules = bucket.lifecycle_rules
    #
    #     print(f"Lifecycle management is disable for bucket {bucket_name} and the rules are {list(rules)}")
    #     return bucket
    #
    # def get_bucket_metadata(bucket_name):
    #     """Prints out a bucket's metadata."""
    #     # bucket_name = 'your-bucket-name'
    #
    #     storage_client = storage.Client()
    #     bucket = storage_client.get_bucket(bucket_name)
    #
    #     print(f"ID: {bucket.id}")
    #     print(f"Name: {bucket.name}")
    #     print(f"Storage Class: {bucket.storage_class}")
    #     print(f"Location: {bucket.location}")
    #     print(f"Location Type: {bucket.location_type}")
    #     print(f"Cors: {bucket.cors}")
    #     print(f"Default Event Based Hold: {bucket.default_event_based_hold}")
    #     print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
    #     print(f"Metageneration: {bucket.metageneration}")
    #     print(
    #         f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
    #     )
    #     print(f"Retention Effective Time: {bucket.retention_policy_effective_time}")
    #     print(f"Retention Period: {bucket.retention_period}")
    #     print(f"Retention Policy Locked: {bucket.retention_policy_locked}")
    #     print(f"Object Retention Mode: {bucket.object_retention_mode}")
    #     print(f"Requester Pays: {bucket.requester_pays}")
    #     print(f"Self Link: {bucket.self_link}")
    #     print(f"Time Created: {bucket.time_created}")
    #     print(f"Versioning Enabled: {bucket.versioning_enabled}")
    #     print(f"Labels: {bucket.labels}")



def manage_bucket():
    operation_required = inputRequests.input_bucket_operation()

    if operation_required == 1:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.create_bucket()

    elif operation_required == 2:
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.delete_bucket()

    elif operation_required == 3:
        storage_class = inputRequests.input_storage_class()
        bucket_name = inputRequests.input_destination_bucket_name()
        bucket = Bucket(bucket_name)
        bucket.update_bucket_storage_class(storage_class)

    else:
        log.warning("No operation found!")
        return


# buc = Bucket()
# buc.list_files("asset_storage_bucket")

# bucket_manager = Bucket()
# bucket_manager.create_bucket("asset_storage_bucket_april")
# bucket_manager.delete_bucket("asset_storage_bucket_april")
