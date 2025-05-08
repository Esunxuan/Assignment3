# server.py
import socket
import threading
import time

tuple_space = {}
lock = threading.Lock()
clients_connected = 0
total_ops = {'PUT': 0, 'GET': 0, 'READ': 0, 'ERR': 0}

def log_stats():
    while True:
        time.sleep(10)
        with lock:
            n = len(tuple_space)
            avg_key = sum(len(k) for k in tuple_space) / n if n else 0
            avg_val = sum(len(v) for v in tuple_space.values()) / n if n else 0
            print(f"--- Server Stats ---")
            print(f"Tuples: {n}, Avg Key: {avg_key:.2f}, Avg Val: {avg_val:.2f}")
            print(f"Clients: {clients_connected}, Ops: {total_ops}")


def handle_client(conn):
    global clients_connected
    with lock:
        clients_connected += 1