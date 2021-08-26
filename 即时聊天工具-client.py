import socket
import time
from threading import Thread

host = '127.0.0.1'
port = 9001
buff = 1024
global s


def receive_message():
    while True:
        rec_msg = str(s.recv(buff), encoding="utf-8")
        if rec_msg == 'Y':
            print('服务端与客户端已经建立连接...')
        elif rec_msg == 'N':
            print('服务端与客户端已经建立连接...')
        else:
            time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print('[%s]: %s' % (time_str, rec_msg))


def send_message():
    while True:
        msg = input('客户端：\n')
        _send(msg)


def _send(msg):
    b = bytes(msg, encoding='utf-8')
    s.sendall(b)


def main():
    global s
    s = socket.socket()
    s.connect((host, port))
    _send('Y')

    rec_thread = Thread(target=receive_message)
    rec_thread.start()

    send_thread = Thread(target=send_message)
    send_thread.start()


if __name__ == '__main__':
    main()