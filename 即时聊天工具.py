import socket
import time
from threading import Thread

host = '127.0.0.1'
port = 9001
buff = 1024

global conn
global addr
global s


def receive_message():
    while True:
        c_msg = str(conn.recv(buff), encoding='utf-8')
        if c_msg == 'Y':
            print('服务端与客户端已经建立连接...')
            _send('Y')
        elif c_msg == 'N':
            print('服务端与客户端已经断开连接...')
            _send('N')
        else:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print('[%s]: %s' % (time_str, c_msg))


def send_message():
    while True:
        msg = input('服务端：\n')
        _send(msg)


def _send(msg):
    b = bytes(msg, encoding='utf-8')
    conn.sendall(b)


def main():
    global s
    global conn, addr
    s = socket.socket()
    s.bind((host, port))
    s.listen(15)
    conn, addr = s.accept()
    print('聊天服务准备就绪...')

    rec_thread = Thread(target=receive_message)
    rec_thread.start()

    send_thread = Thread(target=send_message)
    send_thread.start()


if __name__ == '__main__':
    main()