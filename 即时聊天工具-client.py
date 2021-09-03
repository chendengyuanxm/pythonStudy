import socket
import time
from threading import Thread
import re
import sys

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
        msg = input('>：\n')
        if msg == 'q':
            s.close()
            sys.exit(0)
        else:
            _send(msg)


def _send(msg):
    b = bytes(msg, encoding='utf-8')
    s.sendall(b)


def _input_host():
    is_host = False
    while not is_host:
        host = input('请输入聊天服务器的IP地址:\n')
        result = re.match(r'^\d+\.\d+\.\d+\.\d+$', host)
        if result is None:
            print('IP不合法，请重新输入')
        else:
            is_host = True

    return host


def main():
    global s
    host = _input_host()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置端口可立即重用
    s.connect((host, port))
    _send('Y')

    rec_thread = Thread(target=receive_message)
    rec_thread.start()

    send_thread = Thread(target=send_message)
    send_thread.start()


if __name__ == '__main__':
    main()