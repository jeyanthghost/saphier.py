import os
import subprocess
import time
import shutil

# Function to run Suricata
def run_suricata(interface):
    print(f"Starting Suricata on interface {interface}...")
    # Run Suricata in the background
    subprocess.Popen(["suricata", "-c", "/etc/suricata/suricata.yaml", "-i", interface, "-D"])
    time.sleep(10)  # Wait for Suricata to initialize

# Function to generate malicious logs
def generate_malicious_logs():
    print("Generating malicious logs for 30 seconds...")
    start_time = time.time()
    while time.time() - start_time < 30:
        # Run curl command to generate logs
        subprocess.run(["curl", "http://testmynids.org/uid/index.html"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Function to copy Suricata logs to /var/www/html
def copy_logs_to_web_directory():
    print("Copying Suricata logs to /var/www/html...")
    source_log_path = "/var/log/suricata/eve.json"  # Path to Suricata's log file
    destination_path = "/var/www/html/suricata_logs.json"  # Destination path in web directory

    # Copy the log file to the web directory
    shutil.copy(source_log_path, destination_path)
    print(f"Log file copied to {destination_path}")

# Function to start Apache service
def start_apache():
    print("Starting Apache service...")
    subprocess.run(["systemctl", "start", "apache2"])

# Main function to execute the tasks
def main():
    interface = input("Please enter the network interface name (e.g., eth0, ens33): ")
    run_suricata(interface)
    generate_malicious_logs()
    copy_logs_to_web_directory()
    start_apache()
    print("All tasks completed successfully.")

if __name__ == "__main__":
    main()
