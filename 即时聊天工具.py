import socket
import sys
import time
from threading import Thread

host = socket.gethostbyname(socket.gethostname())
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
        msg = input('>：\n')
        if msg == 'q':
            s.close()
            sys.exit(0)
        else:
            _send(msg)


def _send(msg):
    b = bytes(msg, encoding='utf-8')
    conn.sendall(b)


def main():
    global s
    global conn, addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置端口可立即重用
    s.bind((host, port))
    s.listen(15)
    print('服务器开启[%s:%s]...' % (host, port))
    conn, addr = s.accept()
    print('聊天服务器准备就绪[%s:%s]...' % (host, port))

    rec_thread = Thread(target=receive_message)
    rec_thread.start()

    send_thread = Thread(target=send_message)
    send_thread.start()


if __name__ == '__main__':
    main()