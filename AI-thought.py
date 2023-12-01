import argparse
import socket
import threading
import random
from time import sleep


class Scanner(threading.Thread):
    def __init__(self, host, port, origin_ip):
        super().__init__()
        self.host = host
        self.port = port
        self.origin_ip = origin_ip

    def scan(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.origin_ip, 0))
        s.connect((self.host, self.port))
        return s.recv(1024)

    def run(self):
        result = self.scan()
        if result:
            print("Port {} is open".format(self.port))

        else:
            print("No response from port {} ".format(self.port))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", required=True, help="Host to scan.")
    parser.add_argument("-p", "--ports", default="5060", help="Ports range to scan.")
    parser.add_argument("-o", "--origin-ip", default="127.0.0.1",
                        help="Origin IP to use for the scan.")
    args = parser.parse_args()

    origin_ips = [x.strip() for x in open("/etc/hosts").readlines()]
    random.shuffle(origin_ips)

    scanner = Scanner(args.host, args.ports, origin_ips[0])
    scanner.start()

    while True:
        sleep(5)
        if not threading.activeCount():
            break