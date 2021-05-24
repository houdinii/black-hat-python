import socket


def main():
    target_host = "www.google.com"
    target_port = 80

    # Create Socket Object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client
    client.connect((target_host, target_port))

    # Send some data
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # receive some data
    response = client.recv(4096)

    print(response.decode())
    client.close()


if __name__ == '__main__':
    main()
