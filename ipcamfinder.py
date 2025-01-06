import shodan
import os
import sys

# Shodan API key
API_KEY = ''

def search_shodan(location):
    api = shodan.Shodan(API_KEY)
    try:
        results = api.search(f'location:"{location}"')
        print(f"Found {len(results['matches'])} devices in {location}.")
        for result in results['matches']:
            print(f"IP: {result['ip_str']}, Port: {result['port']}, Product: {result['product']}")
    except shodan.APIError as e:
        print(f"Error searching Shodan: {e}")

def scan_ip(ip):
    print(f"Scanning {ip}...")
    nmap_cmd = f"nmap -p 80,554,8000,8080 -sV {ip}"
    os.system(nmap_cmd)

def main():
    if len(sys.argv) != 2:
        print("Usage: python ipcamera_finder.py <location>")
        sys.exit(1)

    location = sys.argv[1]
    search_shodan(location)

    print("\nScanning IPs for open ports...")
    # Example IPs, replace with actual IPs from Shodan results
    ip_list = ['192.168.1.1', '192.168.1.2']  # Replace with actual IPs
    for ip in ip_list:
        scan_ip(ip)

if __name__ == "__main__":
    main()
