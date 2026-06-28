import socket


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))

    client.sendall(b"Hello, server!")
    data = client.recv(1024)
    print(f"Received: {data.decode()}")

    client.close()


if __name__ == "__main__":
    main()
