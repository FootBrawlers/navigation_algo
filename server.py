
import socket
import i2c_pi as ipi


def server_program():
    # get the hostname
    #host = socket.gethostname()
    host = '192.168.43.31'
    port = 5012 # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data1 = "recieved sucessfully"
        
        conn.send(data1.encode())  # send data to the client
        y = data.split(',')
        a = int(y[0])
        b = int(y[1])
        c = int(y[2])
        d = int(y[3])
        print(a,b,c,d)
        ipi.writeData(a,b,c,d)
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
