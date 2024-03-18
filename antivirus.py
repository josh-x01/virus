import psutil
import sys
import tkinter as tk
from tkinter import messagebox
import os

class AntivirusGUI:
    def __init__(self, master):
        self.master = master
        master.title("Simple Antivirus")

        self.label = tk.Label(
            master, text="Scanning for malicious processes...")
        self.label.pack(pady=10)

        self.scan_button = tk.Button(
            master, text="Scan", command=self.scan_for_malicious_processes)
        self.scan_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=10)

    def find_and_terminate_python_process(self, target_pid):
        try:
            process = psutil.Process(target_pid)
            process.terminate()
            print(f"Python process with PID {target_pid} terminated.")
        except psutil.NoSuchProcess:
            print(f"No process found with PID {target_pid}.")

    def scan_for_malicious_processes(self):
        target_program_names = [
            'annoying-virus.py', 'malicious_program_2.py']

        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_name = process.info['name']
                # Use get to handle the KeyError
                cmdline = process.info.get('cmdline', [])
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

            if process_name == 'python.exe' and any(target_name in cmdline for target_name in target_program_names):
                target_pid = process.info['pid']
                self.find_and_terminate_python_process(target_pid)
                self.show_alert(
                    f"Malicious Python process with PID {target_pid} detected and terminated.")
                return True

        return False

    def show_alert(self, message):
        messagebox.showwarning("Antivirus Alert", message)


def main():
    root = tk.Tk()
    antivirus_gui = AntivirusGUI(root)
    root.mainloop()

def terminate(process_name):
    os.system(f'taskkill /f /im {process_name}')
    return True

if __name__ == "__main__":
    main()
    terminate('Python.exe')
