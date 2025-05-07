python# client.py
import socket
import sys


def send_request(sock, line):
    parts = line.strip().split(" ", 2)
    if not parts:
        return
    if parts[0] == "PUT" and len(parts) >= 3:
        cmd = f"P {parts[1]} {parts[2]}"
    elif parts[0] == "GET" and len(parts) >= 2:
        cmd = f"G {parts[1]}"
    elif parts[0] == "READ" and len(parts) >= 2:
        cmd = f"R {parts[1]}"
    else:
        print(f"Invalid line: {line.strip()}")
        return