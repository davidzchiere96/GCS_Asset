import unittest
from unittest.mock import MagicMock, patch
from components.gcp_lib.cloudClientConnector import CloudStorageClient

class TestCloudStorageClient(unittest.TestCase):

    # patch per mockare le due chiamate
    @patch('components.gcp_lib.cloudClientConnector.storage.Client')
    @patch('components.gcp_lib.cloudClientConnector.Log')
    def test_connect_success(self, mock_log, mock_storage_client):

        # istanziamo un oggetto della classe CloudStorageClient su cui poi fare il test
        cloud_storage_client = CloudStorageClient()

        # chiamiamo il metodo che vogliamo testare
        cloud_storage_client.connect()

        # Assert
        mock_storage_client.assert_called_once()  # Verifica se storage.Client() è stato chiamato esattamente una volta
        # mock_log.info.assert_called_once_with("GCS Client connected!")

    @patch('components.gcp_lib.cloudClientConnector.storage.Client')
    @patch('components.gcp_lib.cloudClientConnector.Log')
    def test_connect_failure(self, mock_log, mock_storage_client):

        # instantiate
        cloud_storage_client = CloudStorageClient()
        mock_storage_client.side_effect = Exception("Connection error")

        # act
        cloud_storage_client.connect()

        # assert
        # mock_log.error.assert_called_once_with("Error connecting to storage client: Connection error")

    @patch('components.gcp_lib.cloudClientConnector.CloudStorageClient.connect')
    def test_get_client_if_not_connected(self, mock_storage_client_connect):

        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.get_client()
        mock_storage_client_connect.assert_called_once()

    @patch('components.gcp_lib.cloudClientConnector.storage.Client')
    def test_get_client_if_connected(self, mock_storage_client):

        cloud_storage_client = CloudStorageClient()
        cloud_storage_client.client = mock_storage_client

        client = cloud_storage_client.get_client()

        self.assertEqual(client, cloud_storage_client.client)


if __name__ == "__main__":
    unittest.main()
