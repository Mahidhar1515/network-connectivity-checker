import subprocess
import platform
import re

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"{host} is UP ✅")
        
        # Try to extract latency
        match = re.search(r'time[=<]\s*(\d+)', result.stdout)
        if match:
            print(f"Latency: {match.group(1)} ms")
    else:
        print(f"{host} is DOWN ❌")

if __name__ == "__main__":
    host = input("Enter website or IP: ")
    ping_host(host)