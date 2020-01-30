
import socket


def client_program():
    #host = socket.gethostname()  # as both code is running on same pc
    host = '192.168.43.31'
    port = 5015  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    #message = input(" -> ")  # take input
    key = input()

    while key.lower().strip() != 'exit':
        if key == 'w':
            message = "1,1,255,255"
        if key == 'a':
            message = "1,2,255,255"
        if key == 's':
            message = "2,2,255,255"
        if key == 'd':
            message = "2,1,255,255"
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        # message = input(" -> ")  # again take input
        key = input()

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
