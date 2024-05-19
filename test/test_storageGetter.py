import unittest
from unittest.mock import MagicMock, patch
from cloudClient import CloudStorageClient
from storageGetter import BucketGetter, FileGetter
import datetime

class TestBucketGetter(unittest.TestCase):

    @patch('storageGetter.CloudStorageClient')
    @patch('storageGetter.Log')
    def test_declare_bucket(self, mock_log, mock_storage_client):
        # Arrange
        bucket_name = "test_bucket"
        mock_client_instance = mock_storage_client.return_value.get_client.return_value

        # Act
        bucket_getter = BucketGetter(bucket_name)
        result = bucket_getter.declare_bucket()

        # Assert
        mock_client_instance.bucket.assert_called_once_with("test_bucket")
        # mock_log.info.assert_called_once_with("Bucket 'test_bucket' declared!")
        self.assertEqual(result, mock_client_instance.bucket.return_value)

    @patch('storageGetter.CloudStorageClient')  # Patchiamo il CloudStorageClient
    @patch('cloudClient.Log')
    def test_get_bucket_success(self, mock_log, mock_cloud_storage_client):
        # Arrange
        bucket_name = "test_bucket"
        mock_client_instance = MagicMock()  # Creiamo un mock dell'istanza del client
        mock_get_bucket = MagicMock()  # Creiamo un mock per il metodo get_bucket
        mock_client_instance.get_bucket = mock_get_bucket  # Configuriamo il mock del client per restituire il mock di get_bucket
        mock_cloud_storage_client.return_value.get_client.return_value = mock_client_instance  # Configuriamo il mock per restituire un'istanza mockata del client

        # Act
        bucket_getter = BucketGetter(bucket_name)
        bucket = bucket_getter.get_bucket()

        # Assert
        self.assertEqual(bucket, mock_get_bucket.return_value)  # Verifichiamo se il bucket restituito è quello restituito dal client mockato
        mock_cloud_storage_client.return_value.get_client.assert_called_once()  # Verifichiamo se il metodo get_client di CloudStorageClient è stato chiamato

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


    @patch('storageGetter.CloudStorageClient.get_client')  # Patchiamo il CloudStorageClient
    @patch('cloudClient.Log')
    def test_list_buckets(self, mock_log, mock_storage_client):
        # mock_list_buckets = MagicMock()
        mock_buckets = [
             MagicMock(name="Bucket1", time_created="2024-05-02T10:30:00", storage_class="STANDARD"),
             MagicMock(name="Bucket2", time_created="2024-05-02T10:30:00", storage_class="NEARLINE")
        ]
        mock_storage_client.return_value.list_buckets.return_value = mock_buckets

        mock_buckets[0].name = "Bucket1"
        mock_buckets[1].name = "Bucket2"

        bucket_getter = BucketGetter()
        result = bucket_getter.list_buckets()

        expected_metadata = [
            {
                'name': "Bucket1",
                'created_time': "2024-05-02T10:30:00",
                'storage_class': "STANDARD"
            },
            {
                'name': "Bucket2",
                'created_time': "2024-05-02T10:30:00",
                'storage_class': "NEARLINE"
            }
        ]

        self.assertEqual(result, expected_metadata)
        mock_storage_client.return_value.list_buckets.assert_called_once_with(prefix=None)


    @patch('storageGetter.CloudStorageClient.get_client')  # Patchiamo il CloudStorageClient
    @patch('cloudClient.Log')
    def test_list_files(self, mock_log, mock_storage_client):
        # mock_list_buckets = MagicMock()
        mock_buckets = [
             MagicMock(name="Bucket1", time_created="2024-05-02T10:30:00", storage_class="STANDARD"),
             MagicMock(name="Bucket2", time_created="2024-05-02T10:30:00", storage_class="NEARLINE")
        ]
        mock_storage_client.return_value.list_buckets.return_value = mock_buckets

        mock_buckets[0].name = "Bucket1"
        mock_buckets[1].name = "Bucket2"

        bucket_getter = BucketGetter()
        result = bucket_getter.list_buckets()

        expected_metadata = [
            {
                'name': "Bucket1",
                'created_time': "2024-05-02T10:30:00",
                'storage_class': "STANDARD"
            },
            {
                'name': "Bucket2",
                'created_time': "2024-05-02T10:30:00",
                'storage_class': "NEARLINE"
            }
        ]

        self.assertEqual(result, expected_metadata)
        mock_storage_client.return_value.list_buckets.assert_called_once_with(prefix=None)




class TestFileGetter(unittest.TestCase):

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('storageGetter.Log')
    def test_declare_file(self, mock_log, mock_storage_client):
        # Arrange
        bucket_name = "test_bucket"
        file_name = "test_file"
        mock_bucket_instance = mock_storage_client.return_value.get_bucket.return_value

        # Act
        file_getter = FileGetter(bucket_name,file_name)
        result = file_getter.declare_file()

        # Assert
        mock_bucket_instance.blob.assert_called_once_with("test_file")
        # mock_log.info.assert_called_once_with("Bucket 'test_bucket' declared!")
        self.assertEqual(result, mock_bucket_instance.blob.return_value)

    @patch('storageGetter.CloudStorageClient.get_client')
    @patch('cloudClient.Log')
    def test_get_file_success(self, mock_log, mock_storage_client):
        # Arrange
        bucket_name = "test_bucket"
        file_name = "test_file"
        mock_bucket_instance = MagicMock()  # Creiamo un mock dell'istanza del client
        mock_get_blob = MagicMock()  # Creiamo un mock per il metodo get_bucket
        mock_bucket_instance.get_blob = mock_get_blob  # Configuriamo il mock del client per restituire il mock di get_bucket
        mock_storage_client.return_value.get_bucket.return_value = mock_bucket_instance  # Configuriamo il mock per restituire un'istanza mockata del client

        # Act
        file_getter = FileGetter(bucket_name,file_name)
        result = file_getter.get_file()

        # Assert
        mock_storage_client.return_value.get_bucket.assert_called_once()
        self.assertEqual(result, mock_get_blob.return_value)


    @patch('cloudClient.storage.Client')
    @patch('cloudClient.Log')
    def test_get_file_failure(self, mock_log, mock_storage_client):
        # instantiate
        cloud_storage_client = CloudStorageClient()
        mock_storage_client.side_effect = Exception("Connection error")

        # act
        cloud_storage_client.connect()

        # assert
        # mock_log.error.assert_called_once_with("Error connecting to storage client: Connection error")

    # TODO: def test_file_size


if __name__ == "__main__":
    unittest.main()
