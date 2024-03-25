import unittest
from unittest.mock import patch, MagicMock
import getStorageBucket
import cloudStorage

class TestGetStorageBucket(unittest.TestCase):
    @patch('getStorageBucket.cloudStorage.storage_client')
    def test_get_bucket(self, mock_storage_client):
        # Simuliamo il comportamento di storage_client()
        mock_client = MagicMock()
        mock_storage_client.return_value = mock_client

        # Chiamiamo la funzione get_bucket()
        bucket_name = "asset_storage_bucket"
        bucket = getStorageBucket.get_bucket(bucket_name)

        mock_storage_client.assert_called_once()

        mock_client.get_bucket.assert_called_once_with(bucket_name)

        # Verifichiamo che il client sia stato creato correttamente
        self.assertIsInstance(bucket, MagicMock)

if __name__ == "__main__":
    unittest.main()