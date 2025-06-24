import socket
import requests

def scan_ports(ip):
    print(f"\nScanning {ip} for open ports...\n")
    for port in range(1, 101):  # Scan ports 1 to 100
        try:
            s = socket.socket()
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except:
            pass

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.settimeout(2)
        banner = s.recv(1024).decode().strip()
        print(f"\nBanner on port {port}: {banner}")
        s.close()
    except:
        print(f"\nCould not grab banner from port {port}")

def brute_force_login(url, username, passwords):
    print(f"\nStarting brute-force on {url} with username '{username}'...\n")
    for pwd in passwords:
        data = {'username': username, 'password': pwd.strip()}
        try:
            response = requests.post(url, data=data)
            if "invalid" not in response.text.lower():
                print(f"Login successful! Password is: {pwd}")
                return
        except:
            print("Error connecting to the site.")
    print("Brute-force failed. Password not found.")


print("Penetration Testing Toolkit")
print("===========================")

target_ip = input("\nEnter the Target IP Address: ")
scan_ports(target_ip)
grab_banner(target_ip, 80)

choice = input("\nDo you want to run brute-force on a test site? (yes/no): ").lower()
if choice == 'yes':
    test_url = "http://testphp.vulnweb.com/login.php"  # Safe test site
    username = "admin"
    passwords = ["admin", "1234", "admin123", "password", "root"]
    brute_force_login(test_url, username, passwords)

print("\n Scan Completed. Happy Hacking (Ethically)! ")