import unittest
from unittest.mock import MagicMock, patch
#import gcs_asset.cloudStorage #import storage_client
from src.getStorageBucket import get_bucket_name
#from test_cloudStorage import TestStorageClient
import test_cloudStorage

import sys
import os

# Add the directory containing cloudStorage.py to the Python path
sys.path.append(os.path.abspath(r'C:\Users\ECHIERDF9\PycharmProjects\GCS_Asset_pythonProject\gcs_asset\cloudStorage.py'))

# Now you can import cloudStorage
import cloudStorage


class TestGetStorageBucket(unittest.TestCase):

    @patch("test_cloudStorage.test_storage_client")
    def test_get_bucket_name(self, mock_storage_client):
        # Creiamo un mock per il client di Google Cloud Storage
        mock_client = MagicMock()
        mock_bucket = MagicMock()
        mock_client.get_bucket.return_value = mock_bucket
        mock_storage_client.return_value = mock_client
        #TestStorageClient.test_storage_client.return_value = mock_client

        # Chiamiamo la funzione get_bucket_name
        result = get_bucket_name()

        # Verifichiamo che il mock della funzione storage_client sia stato chiamato
        mock_client.assert_called_once()

        # Verifichiamo che il mock della funzione get_bucket sia stato chiamato con il nome del bucket corretto
        mock_bucket.assert_called_once_with("asset_storage_bucket")
        #mock_client.get_bucket.assert_called_once_with("asset_storage_bucket")

        # Verifichiamo che il risultato sia quello atteso
        self.assertEqual(result, mock_bucket)


if __name__ == '__main__':
    unittest.main()
