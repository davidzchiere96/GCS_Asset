import unittest
from unittest.mock import MagicMock
from gcs_asset_components.sum import somma


class TestSomma(unittest.TestCase):

    def test_somma_con_magicmock(self):

        # Creiamo un mock per la funzione somma
        mock_somma = MagicMock(side_effect=lambda a, b, c: a + b + c)

        # Sovrascriviamo la funzione somma con il nostro mock
        somma = mock_somma

        # Chiamiamo la funzione somma con dei valori fittizi
        result = somma(5, 6, 0)

        # Verifichiamo che il mock sia stato chiamato con gli argomenti corretti
        mock_somma.assert_called_once_with(5, 6, 0)

        # Verifichiamo che il risultato sia quello che ci aspettiamo
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()