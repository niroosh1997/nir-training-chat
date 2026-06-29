import socket


class ClientHandler:
    def __init__(self, connection: socket.socket):
        self._connection = connection

    def handle_message(self, msg: str):
        pass
