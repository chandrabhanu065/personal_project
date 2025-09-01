import subprocess
import time
from datetime import datetime

app_name = "Google Chrome"

# Get PID of the app using pgrep
try:
    pid = subprocess.check_output(["pgrep", app_name]).decode().strip().split('\n')[0]
except subprocess.CalledProcessError:
    print(f"Process '{app_name}' not found.")
    exit(1)

print(f"Monitoring PID {pid} for application '{app_name}'...")

for _ in range(60):
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Run 'top -l 1 -pid <pid>' and filter the output
    top_output = subprocess.check_output(["top", "-l", "1", "-pid", pid]).decode()
    
    # Filter lines that contain the app name
    for line in top_output.splitlines():
        if app_name in line:
            print(line)
            break

    time.sleep(1)

