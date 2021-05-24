import socket


def main():
    target_host = "127.0.0.1"
    target_port = 9998

    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Send some data
    client.connect((target_host, target_port))
    client.send(b"AAABBBCCC")

    # Receive some data
    data, addr = client.recvfrom(4096)

    print(data.decode())
    client.close()


if __name__ == '__main__':
    main()
