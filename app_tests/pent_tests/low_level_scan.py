import sys
import subprocess
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python3 low_level_scan.py <target>")
    sys.exit(1)

target = sys.argv[1]
log_file = f"log_files/low_level_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
touch = subprocess.run(["touch",log_file])

with open(log_file, "w") as f:
    f.write(f"Low Level Penetration Test Results for {target}\n\n")
    # Nmap basic port scan
    f.write("--- Nmap Scan ---\n")
    nmap_cmd = ["nmap","-sT","localhost"]
    nmap_result = subprocess.run(nmap_cmd, capture_output=True, text=True)
    f.write(nmap_result.stdout)
    f.write("\n")
    # Nikto basic web server scan
    f.write("--- Nikto Scan ---\n")
    nikto_cmd = ["nikto", "-h", target]
    nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)
    f.write(nikto_result.stdout)
    f.write("\n")

print(f"Low level scan complete. Results saved to {log_file}")
