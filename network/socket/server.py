import socket


def start_server(host, port):
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    # start server, one thread, only one connection one time
    while(True):
        # will block until client connect
        connection, addr = server.accept()

        msg = 'welcome to jkcloud'
        print('send msg: {}'.format(msg))
        connection.send(msg)

        # will block until message comming
        msg = connection.recv(1024)
        print('receive msg: {}'.format(msg))

        msg = 'please close connection'
        print('send msg: {}'.format(msg))
        connection.send(msg)

        print('close connection')
        # close connection
        connection.close()


if __name__ == '__main__':
    start_server('127.0.0.1', 1948)
