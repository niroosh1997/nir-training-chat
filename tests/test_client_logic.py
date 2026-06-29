from unittest.mock import Mock

from nir_training.client_handler import ClientHandler


def test_client_first_connection():
    client_handler = ClientHandler(Mock())
    client_handler.handle_message(b"heyyy")
