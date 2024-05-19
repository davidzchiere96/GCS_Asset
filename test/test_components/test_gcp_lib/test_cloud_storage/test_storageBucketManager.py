import unittest
from unittest.mock import MagicMock, patch
from components.gcp_lib.cloudClientConnector import CloudStorageClient
from components.gcp_lib.cloud_storage.storageGetter import BucketGetter, FileGetter
from components.gcp_lib.cloud_storage.storageBucketManager import Bucket

class TestBucket(unittest.TestCase):

    @patch('components.gcp_lib.cloud_storage.storageGetter.CloudStorageClient.get_client')  # Patchiamo il CloudStorageClient
    def test_create_bucket(self, mock_cloud_storage_client, local_zone="eu", storage_class="Standard"):
        # Arrange
        bucket_name = "test_bucket"
        mock_client_instance = MagicMock()  # Creiamo un mock dell'istanza del client
        mock_create_bucket = MagicMock()  # Creiamo un mock per il metodo get_bucket
        mock_client_instance.create_bucket = mock_create_bucket  # Configuriamo il mock del client per restituire il mock di get_bucket
        mock_cloud_storage_client.return_value.create_bucket.return_value = mock_client_instance  # Configuriamo il mock per restituire un'istanza mockata del client

        # Act
        bucket = Bucket(bucket_name)
        create_bucket = bucket.create_bucket(local_zone="eu", storage_class="Standard")

        # Assert
        self.assertEqual(create_bucket, mock_client_instance)  # Verifichiamo se il bucket restituito è quello restituito dal client mockato
        mock_cloud_storage_client.return_value.create_bucket.assert_called_once()  # Verifichiamo se il metodo get_client di CloudStorageClient è stato chiamato

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('cloudClient.Log')
    def test_get_bucket_success(self, mock_log, mock_storage_client):

        bucket_getter = BucketGetter("test_bucket")
        # cloud_storage_client = cloud_storage_instance.__storage_client
        # cloud_storage_instance = CloudStorageClient()
        # cloud_storage_client = cloud_storage_instance.get_client()

        bucket = bucket_getter.get_bucket()

        self.assertEqual(bucket,mock_storage_client.get_bucket())
        mock_storage_client.return_value.get_client.assert_called_once()

        # cloud_storage_client.get_bucket("test_bucket")
        # mock_get_bucket = mock_storage_client.get_bucket("test_bucket")

       #  mock_storage_client.assert_called_once()
       # mock_get_bucket.assert_called_once()
        # mock_log.info.assert_called_once_with("GCS Client connected!")

    @patch('cloudClient.storage.Client')
    @patch('cloudClient.Log')
    def test_get_bucket_failure(self, mock_log, mock_storage_client):

        # instantiate
        cloud_storage_client = CloudStorageClient()
        mock_storage_client.side_effect = Exception("Connection error")

        # act
        cloud_storage_client.connect()

        # assert
        # mock_log.error.assert_called_once_with("Error connecting to storage client: Connection error")

    # TODO: def test_list_buckets
    # TODO: def test_list_files



if __name__ == "__main__":
    unittest.main()
