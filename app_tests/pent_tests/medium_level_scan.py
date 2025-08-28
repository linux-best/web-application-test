import sys
import subprocess
from datetime import datetime

if len(sys.argv) != 2:
    print("Usage: python3 medium_level_scan.py <target>")
    sys.exit(1)

target = sys.argv[1]
log_file = f"log_files/medium_level_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
touch = subprocess.run(["touch",log_file])


with open(log_file, "w") as f:
    f.write(f"Medium Level Penetration Test Results for {target}\n\n")
    # Nmap service/version detection
    f.write("--- Nmap Service/Version Detection ---\n")
    nmap_cmd = ["nmap", "-sV", target]
    nmap_result = subprocess.run(nmap_cmd, capture_output=True, text=True)
    f.write(nmap_result.stdout)
    f.write("\n")
    # Nikto scan
    f.write("--- Nikto Scan ---\n")
    nikto_cmd = ["nikto", "-h", target]
    nikto_result = subprocess.run(nikto_cmd, capture_output=True, text=True)
    f.write(nikto_result.stdout)
    f.write("\n")
    # SQLMap basic test
    f.write("--- SQLMap Test ---\n")
    sqlmap_cmd = ["sqlmap", "-u", target, "--batch"]
    sqlmap_result = subprocess.run(sqlmap_cmd, capture_output=True, text=True)
    f.write(sqlmap_result.stdout)
    f.write("\n")
    # Dirsearch directory brute-force
    f.write("--- Dirsearch Scan ---\n")
    dirsearch_cmd = ["dirsearch", "-u", target]
    dirsearch_result = subprocess.run(dirsearch_cmd, capture_output=True, text=True)
    f.write(dirsearch_result.stdout)
    f.write("\n")

print(f"Medium level scan complete. Results saved to {log_file}")
