import tkinter as tk
from tkinter import simpledialog
from tkinter import *
import shutil
import os
import subprocess
import tkinter.ttk as ttk
import ttkbootstrap
import threading
import http.server
import socketserver
import webbrowser
import socket
from server import start_server, stop_server

print("Welcome to the Profit and Loss Generator!")
# Server related variables
directory = r'C:\Users\andre\PycharmProjects\PL_GPT_Approach'
server_thread = None
httpd = None


def prompt_filename():
    filename = simpledialog.askstring("Filename", "Please enter the filename:")
    if filename:  # only process if a filename was entered
        # Create the new file
        template_filename = '../csvs/samples.csv'
        new_filename = f'../csvs/{filename}.csv'
        shutil.copyfile(template_filename, new_filename)

        # Save the filename to a text file
        with open('filename.txt', 'w') as f:
            f.write(filename)

        # Open the new file
        os.startfile(os.path.abspath(new_filename))


# def start_serv():
#     # Execute the start_server.py script
#     subprocess.Popen(['python', 'start_server.py'])
#
#
# def stop_serv():
#     # Execute the stop_server.py script
#     subprocess.Popen(['python', 'stop_server.py'])


def run_data_for_pl():
    subprocess.Popen(['python', 'pl_compl.py'])

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

def run_data_for_pl():
    subprocess.Popen(['python', 'pl_compl.py'])

def on_closing():
    stop_server()
    root.destroy()

# Initialize the styled tkinter
root = tk.Tk()
style = ttkbootstrap.Style('lumen')

root.title("Profit and Loss Generator")
root.geometry("500x500")
root.configure(bg="#DDE5B6")


# Label for step 1
ttk.Label(root, text="Step 1: Enter Filename", style='primary.TLabel').pack(pady=(20, 0))

# Button for step 1
filename_button = ttk.Button(root, text="Enter Filename", command=prompt_filename, style='info.Outline.TButton')
filename_button.pack(pady=10)

# Label for step 2
ttk.Label(root, text="Step 2: Run Data for PL", style='primary.TLabel').pack(pady=(20, 0))

# Button for step 2
data_button = ttk.Button(root, text="Run Data for PL", command=run_data_for_pl, style='warning.Outline.TButton', width=50)
data_button.pack(pady=10)

# Label for step 3
ttk.Label(root, text="Step 3: Start Server", style='primary.TLabel').pack(pady=(20, 0))

# Button for step 3
start_button = ttk.Button(root, text="Start Server", command=start_server, style='danger.Outline.TButton')
start_button.pack(pady=10)

# Label for step 4
ttk.Label(root, text="Step 4: Stop Server", style='primary.TLabel').pack(pady=(20, 0))

# Button for step 4
stop_button = ttk.Button(root, text="Stop Server", command=stop_server, style='danger.Outline.TButton')
stop_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()



