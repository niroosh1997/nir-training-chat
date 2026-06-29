import socket
import threading

from nir_training.client_logic import ClientLogic


class Server:
    def run(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.bind(("127.0.0.1", 9999))
                s.listen()
                while True:
                    conn, addr = s.accept()
                    thread = threading.Thread(
                        target=self._handle_client, args=(conn, addr)
                    )
                    thread.daemon = True
                    thread.start()
        except KeyboardInterrupt:
            print("Get out!")

    def _handle_client(self, connection: socket.socket, address: tuple[str, int]):
        client_logic = ClientLogic(connection)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            client_logic.handle_message(data)


if __name__ == "__main__":
    server = Server()
    server.run()
