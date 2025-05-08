# server.py
import socket
import threading
import time

tuple_space = {}
lock = threading.Lock()
clients_connected = 0
total_ops = {'PUT': 0, 'GET': 0, 'READ': 0, 'ERR': 0}