"""This scripts is used to start the local tracking server.
"""

import subprocess
import mlflow

SERVER_HOST = "127.0.0.1"
SERVER_PORT = "8080"

def configure_server():
    mlflow.set_tracking_uri(uri=f"http://{SERVER_HOST}:{SERVER_PORT}")

def start_tracking_server():
    """Start the local tracking server.
    """
    # Start the tracking server
    subprocess.Popen(["mlflow", "server", "--host", SERVER_HOST, "--port", SERVER_PORT])
