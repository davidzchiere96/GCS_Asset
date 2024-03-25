import unittest
from unittest.mock import MagicMock
from cloudStorage import storage_client
from google.cloud import storage

import unittest
from unittest.mock import patch, MagicMock
import cloudStorage

class TestStorageClient(unittest.TestCase):
    @patch('cloudStorage.storage.Client.from_service_account_json')
    def test_storage_client(self, mock_from_service_account_json):
        # Chiamiamo la funzione storage_client
        client = cloudStorage.storage_client()

        # Verifichiamo che la funzione from_service_account_json sia stata chiamata
        mock_from_service_account_json.assert_called_once_with(json_credentials_path='config\smooth-tesla-413121-a1ac05929582.json')

        # Verifichiamo che il client sia stato creato correttamente
        self.assertIsInstance(client, MagicMock)

if __name__ == "__main__":
    unittest.main()