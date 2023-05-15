import http.server
import socketserver
import webbrowser
import os
import socket

# Specify the directory containing the index.html file
directory = r'C:\Users\andre\PycharmProjects\PL_GPT_Approach'

# Change to the specified directory
os.chdir(directory)

# Create a new socket and bind to a random port, then close it and use that port number for the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 0))
port = sock.getsockname()[1]
sock.close()

# Start the local server
httpd = socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler)

# Open the index.html file in a web browser
webbrowser.open(f"http://localhost:{port}/index.html")

# Serve the files indefinitely until interrupted
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

# Close the server
httpd.server_close()