import os
import subprocess
import time
import shutil

# Function to run Suricata
def run_suricata(interface):
    print(f"Starting Suricata on interface {interface}...")
    subprocess.Popen(["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", interface, "-D"])
    time.sleep(10)  # Wait for Suricata to initialize

# Function to generate malicious logs
def generate_malicious_logs():
    print("Generating malicious logs for 30 seconds...")
    start_time = time.time()
    while time.time() - start_time < 30:
        subprocess.run(["curl", "http://testmynids.org/uid/index.html"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Function to copy Suricata logs to /var/www/html
def copy_logs_to_web_directory():
    print("Copying Suricata logs to /var/www/html...")
    source_log_path = "/var/log/suricata/eve.json"
    destination_path = "/var/www/html/suricata_logs.json"

    shutil.copy(source_log_path, destination_path)
    print(f"Log file copied to {destination_path}")

# Function to start Apache service
def start_apache():
    print("Starting Apache service...")
    subprocess.run(["systemctl", "start", "apache2"])

# Function to start ngrok service
def start_ngrok():
    print("Starting Ngrok service...")
    ngrok_command = "ngrok http --url=magnetic-clam-correctly.ngrok-free.app 80"
    subprocess.Popen(ngrok_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Main function to execute the tasks
def main():
    interface = input("Please enter the network interface name (e.g., eth0, ens33): ")
    if not interface:
        print("Input Error: Please enter a valid network interface name.")
        return

    try:
        run_suricata(interface)
        time.sleep(5)  # Wait a bit for Suricata to start capturing traffic
        generate_malicious_logs()
        time.sleep(5)  # Wait a bit for logs to be generated
        copy_logs_to_web_directory()
        start_apache()
        start_ngrok()  # Start ngrok after Apache
        print("All tasks completed successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
