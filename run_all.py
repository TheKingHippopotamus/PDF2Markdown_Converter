import subprocess
import sys
import os
import signal

processes = []

try:
    print("Starting PDF2MD Monitor...")
    monitor_proc = subprocess.Popen([sys.executable, "monitor.py"])
    processes.append(monitor_proc)

    print("Starting PDF2MD File Manager...")
    gui_proc = subprocess.Popen([sys.executable, "pdf2md_gui.py"])
    processes.append(gui_proc)

    print("Starting PDF2MD Chat with Ollama...")
    chat_proc = subprocess.Popen([sys.executable, "chat_with_ollama.py"])
    processes.append(chat_proc)

    print("All apps started! Press Ctrl+C to close all.")
    # Wait for all processes
    for proc in processes:
        proc.wait()
except KeyboardInterrupt:
    print("\nShutting down all apps...")
    for proc in processes:
        try:
            proc.terminate()
        except Exception:
            pass
    for proc in processes:
        try:
            proc.wait(timeout=5)
        except Exception:
            pass
    print("All apps closed.")
