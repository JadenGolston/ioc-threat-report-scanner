# Simple IOC scanner that flags known bad domains and IPs in log files

bad_ips = ["185.225.69.69", "45.155.205.233"]
bad_domains = ["update-checker.ru", "secure-host.cc"]

with open("sample_data.txt", "r") as f:
    lines = f.readlines()

print("🔍 Scanning for IOCs...\n")

for line in lines:
    for ip in bad_ips:
        if ip in line:
            print(f"[!] Malicious IP found: {ip}")
    for domain in bad_domains:
        if domain in line:
            print(f"[!] Malicious Domain found: {domain}")
