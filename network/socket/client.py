import socket


def get_client(host, port):
    client = socket.socket()
    client.connect((host, port))

    # block method
    msg = client.recv(1024)
    print('receive msg: {}'.format(msg))

    msg = 'thank you'
    print('send msg: {}'.format(msg))
    client.send(msg)

    msg = client.recv(1024)
    print('receive msg: {}'.format(msg))

    print('close connection')
    client.close()


if __name__ == '__main__':
    get_client('127.0.0.1', 1948)
