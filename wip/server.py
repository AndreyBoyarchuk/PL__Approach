import http.server
import socketserver
import webbrowser
import os
import socket
import threading

# Server related variables
directory = r'C:\Users\andre\PycharmProjects\PL_GPT_Approach'
server_thread = None
httpd = None

def start_server():
    global server_thread, httpd
    if server_thread is None:
        os.chdir(directory)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        sock.close()
        httpd = socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler)
        webbrowser.open(f"http://localhost:{port}/index.html")
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()

def stop_server():
    global server_thread, httpd
    if server_thread is not None:
        httpd.shutdown()
        httpd.server_close()
        server_thread.join()
        server_thread = None
        httpd = None
