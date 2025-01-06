# ipcamfinder

## Description
`ipcamfinder` is a Python tool designed to help identify exposed IP cameras using the Shodan API. It allows you to search for IP cameras in a specific location, scan a single IP address for open ports, or scan multiple IP addresses from a file.

## Features
- Search Shodan for devices in a specified location.
- Scan a specific IP address for open ports commonly used by IP cameras.
- Scan multiple IP addresses from a file.

## Installation

### Clone the Repository
```bash
git clone https://github.com/giridarane/ipcamfinder.git
cd ipcamfinder
```

### Install Requirements
```bash
pip install -r requirements.txt
```

## Usage

### Search by Location
To search for IP cameras in a specific location (e.g., "New York"):
```bash
python ipcamfinder.py -l "New York"
```

### Scan a Specific IP
To scan a specific IP address for open ports:
```bash
python ipcamfinder.py -ip 192.168.1.1
```

### Scan Multiple IPs from a File
To scan multiple IP addresses from a file:
```bash
python ipcamfinder.py -f ips.txt
```
The file should contain one IP address per line:
```text
192.168.1.1
192.168.1.2
10.0.0.1
```

## Requirements
The tool requires the following Python libraries:
- `shodan`
- `argparse`
- `os`
- `sys`

### Shodan API Key
To use this tool, you must have a valid Shodan API key. You can obtain one by creating an account on [Shodan](https://www.shodan.io/). Once you have the API key, add it to the `ipcamfinder.py` file:
```python
API_KEY = 'your_shodan_api_key_here'
```
