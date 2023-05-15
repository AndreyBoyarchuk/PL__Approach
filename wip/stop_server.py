import requests

def stop_server():
    # Send a GET request to the server's shutdown endpoint
    response = requests.get("http://localhost:8000/shutdown")

    # Check the response status code to ensure successful shutdown
    if response.status_code == 200:
        print("Server stopped successfully.")
    else:
        print("Failed to stop the server.")

# Call the stop_server function
stop_server()