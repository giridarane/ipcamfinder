import shodan
import os
import sys
import argparse

# Shodan API key
API_KEY = ''

def search_shodan(location):
    api = shodan.Shodan(API_KEY)
    try:
        results = api.search(f'location:"{location}"')
        print(f"Found {len(results['matches'])} devices in {location}.")
        for result in results['matches']:
            print(f"IP: {result['ip_str']}, Port: {result['port']}, Product: {result.get('product', 'N/A')}")
    except shodan.APIError as e:
        print(f"Error searching Shodan: {e}")

def scan_ip(ip):
    print(f"Scanning {ip}...")
    nmap_cmd = f"nmap -p 80,554,8000,8080 -sV {ip}"
    os.system(nmap_cmd)

def scan_ips_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ips = file.readlines()
        for ip in ips:
            ip = ip.strip()
            if ip:
                scan_ip(ip)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="IP Camera Finder Tool using Shodan API")
    parser.add_argument('-l', '--location', help='Location to search for IP cameras (e.g., "New York")')
    parser.add_argument('-ip', '--scan-ip', help='Specific IP to scan for open ports')
    parser.add_argument('-f', '--file', help='File containing a list of IPs to scan')

    args = parser.parse_args()

    if args.location:
        search_shodan(args.location)
    elif args.scan_ip:
        scan_ip(args.scan_ip)
    elif args.file:
        scan_ips_from_file(args.file)
    else:
        print("Please provide a valid option. Use -h for help.")
        sys.exit(1)

if __name__ == "__main__":
    main()
