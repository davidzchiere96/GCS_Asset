import unittest
from unittest.mock import MagicMock
from gcs_asset_components.cloudStorage import storage_client, storage

class TestStorageClient(unittest.TestCase):

    def test_storage_client(self):
        # Creiamo un mock per il client di Google Cloud Storage
        mock_storage_client = MagicMock()

        # Sovrascriviamo la funzione storage_client con il nostro mock
        storage.Client.from_service_account_json = MagicMock(return_value=mock_storage_client)

        # Chiamiamo la funzione storage_client
        result = storage_client()

        # Verifichiamo che il mock sia stato chiamato correttamente
        storage.Client.from_service_account_json.assert_called_once()

        # Verifichiamo che il risultato sia quello che ci aspettiamo
        self.assertEqual(result, mock_storage_client)

if __name__ == '__main__':
    unittest.main()
