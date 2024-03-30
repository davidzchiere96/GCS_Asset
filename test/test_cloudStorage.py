import unittest
from unittest.mock import MagicMock, patch

# Importa il modulo in cui è definita la classe StorageClient
from cloudStorageClient import StorageClient

class TestStorageClient(unittest.TestCase):
    # Test della classe StorageClient
    def test_storage_client(self):
        # Crea un mock per il client di storage
        mock_client = MagicMock()

        # Patch del client di storage con il mock creato sopra
        with patch('cloudStorageClient.storage.Client', return_value=mock_client) as mock_storage_client:
            # Crea un'istanza di StorageClient
            storage_client = StorageClient()

            # Verifica che il metodo connect venga chiamato
            storage_client.connect()

            # Verifica che il metodo get_client restituisca il client di storage mockato
            self.assertEqual(storage_client.get_client(), mock_client)

    # Test per la connessione al client di storage
    def test_storage_client_connection(self):
        # Crea un mock per il logger
        mock_logger = MagicMock()

        # Patch del logger con il mock creato sopra
        with patch('cloudStorageClient.logger.logger', return_value=mock_logger) as mock_logger:
            # Crea un'istanza di StorageClient
            storage_client = StorageClient()

            # Verifica che il metodo connect venga chiamato correttamente
            storage_client.connect()

            # Verifica che il logger venga chiamato con il messaggio di errore corretto in caso di errore di connessione
            mock_logger.error.assert_not_called()  # Assicurati che il logger non sia chiamato se la connessione ha successo

if __name__ == "__main__":
    unittest.main()
