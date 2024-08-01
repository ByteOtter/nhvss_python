import os
import time
import vulnerability_scan

from pathlib import Path


def vuln_scan_switch() -> bool:
    """
    Toggle vulnerability scans on or off.

    Returns:
    bool: True if the input is 'y', False if it is 'N'.

    Will retry the question for invalid input.
    """
    while True:
        user_input = (
            input("Would you to scan for vulnerabilities? (y/n): ").strip().lower()
        )

        if user_input not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.")
        else:
            break

    # Assign based on user input
    vuln_scan = True if user_input.lower() == "y" else False

    if vuln_scan:
        print("The computer will scan for vulnerabilities")
    else:
        print("The computer will not scan for vulnerabilities")

    return vuln_scan


def validate_ip(ip: str) -> bool:
    """
    Check if the input is a valid IPv4 adress.

    Args:
    ip (str): The string of the IP address to validate.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    # Check if each part of the ip address is an integer in a valid range of 0 to 255.
    try:
        return all(0 <= int(part) < 256 for part in ip.split("."))
    except ValueError:
        return False


vuln_scan = vuln_scan_switch()

# Create config.txt if it does not exist.
if not Path.cwd().rglob("config.txt"):
    Path("config.txt").touch()

content = []

print("Scanning the network")

while True:
    ip = input("Enter the ip address of the network you would like to scan: ")

    if not validate_ip(ip):
        print("Invalid Ipv4 format. Try again.")
    else:
        break

# Construct base IP address by taking the first three octets from the user's input
base_ip = "{}.{}.{}".format(*ip.split(".")[:3])

# Iterate over last octet to scan the whole subnet
for i in range(10):
    ip_scan = "{}.{}".format(base_ip, i)
    print("Scanning " + ip_scan)
    response = os.popen("sudo nmap -sS {}".format(ip_scan)).read()

    if "Host seems down" in response:
        print("{} is down\n".format(ip_scan))
    else:
        host_info = os.popen("host {}".format(ip_scan)).read()
        host_line = host_info.split("\n")[0].split()[4]  # Assuming the 5th word is the hostname
        print("The host is: " + host_line)

        # Append IP address and its status to content list
        content.append(
            "{} | {}{}\n".format(
                ip_scan, host_line, " is up" if not "down" in response else ""
            )
        )
        time.sleep(1)

file_name = time.strftime("%Y-%m-%d_%H-%M-%S") + "_hosts.txt"
# Create scan_history directory if it does not exist.
scan_history_dir = Path("scan_history")
scan_history_dir.mkdir(parents=True, exist_ok=True)

file_path = scan_history_dir / file_name
file_path.touch()

with open("config.txt", "r") as file:
    content_config = file.read()
    file.close()

if content.__contains__("newest scan = "):
    with open("config.txt", "w") as file:
        file.write("newest scan = scan_history/" + file_name)
        file.close()
else:
    with open("config.txt", "w") as file:
        file.write("newest scan = scan_history/" + file_name)
        file.close()

try:
    with open("scan_history/" + file_name, "a") as file:
        for content in content:
            file.write(content)
        file.close()
except FileNotFoundError:
    print("Error: File {} not found!")
    exit(1)

#print(ip + " is up \n")
print("Networkmapping completed")

print("\nStarting vulnerability scan")

if vuln_scan:
    vulnerability_scan.vulnerability_scan(file_name)

print("\nVulnerability scan completed")
