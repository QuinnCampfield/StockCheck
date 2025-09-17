#!/usr/bin/env python3
"""
Startup script that runs both FastAPI and Streamlit services
"""
import subprocess
import threading
import time
import os
import signal
import sys

def run_api():
    """Run the FastAPI server"""
    print("Starting FastAPI server...")
    subprocess.run([
        "uvicorn", "app:app", 
        "--host", "0.0.0.0", 
        "--port", "8000"
    ])

def run_streamlit():
    """Run the Streamlit server"""
    print("Starting Streamlit server...")
    port = os.getenv("PORT", "8501")
    subprocess.run([
        "streamlit", "run", "streamlit_app.py",
        "--server.port", port,
        "--server.address", "0.0.0.0"
    ])

def signal_handler(sig, frame):
    """Handle shutdown signals"""
    print("\nShutting down services...")
    sys.exit(0)

if __name__ == "__main__":
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Start API in a separate thread
    api_thread = threading.Thread(target=run_api, daemon=True)
    api_thread.start()
    
    # Give API time to start
    time.sleep(2)
    
    # Start Streamlit (main process)
    run_streamlit()
