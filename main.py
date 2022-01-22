import socket
import sys
import threading


def connect(PORT):
    thread_name = threading.current_thread().name.replace("(connect)", "")
    s = socket.socket()
    try:
        s.connect((HOST, PORT))
        s.settimeout(5)
    except:
        pass
    else:
        with print_lock:
            print(f'[{thread_name}] {s.getsockname()} = OPEN.')
    finally:
        s.close()


print_lock = threading.Lock()
HOST = '127.0.0.1'

if len(sys.argv) > 1:
    HOST = str(sys.argv[1])

for PORT in range(1, 100000):
    while threading.active_count() > 200:
        pass
    thread = threading.Thread(target=connect, args=(PORT,))
    thread.start()
