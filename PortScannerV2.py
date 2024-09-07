import os
import socket
import concurrent.futures
from time import sleep
from prettytable import PrettyTable
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
# t.me/LordDigital_LD
try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found, installing...")
    install("tqdm")

try:
    from prettytable import PrettyTable
except ImportError:
    print("PrettyTable not found, installing...")
    install("prettytable")
# t.me/LordDigital_LD
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def display_banner():
    banner = """
===============================================================================   
 ____            _     ____                                   __     ______
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __  \ \   / /___ \\
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  \ \ / /  __) |
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |      \ V /  / __/
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|       \_/  |_____|

                         Telegram: @LordDigitdl_LD
===============================================================================
"""
    print(banner)
# t.me/LordDigital_LD
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((host, port))
    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
        except:
            service = "unknown"
        finally:
            sock.close()
        return port, service
    sock.close()
    return None
# t.me/LordDigital_LD
def scan_ports(host, ports):
    open_ports = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = list(tqdm(executor.map(lambda port: scan_port(host, port), ports), total=len(ports), desc="Scanning Ports"))
    for result in results:
        if result:
            port, service = result
            open_ports[port] = service
    return open_ports
# t.me/LordDigital_LD
def write_to_file(filename, open_ports):
    with open(filename, "w") as file:
        for port, service in open_ports.items():
            file.write(f"{port} = {service}\n")
# t.me/LordDigital_LD
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# t.me/LordDigital_LD
def loading_animation():
    clear_screen()
    for _ in range(3):
        for frame in ["Loading .", "Loading ..", "Loading ..."]:
            print(frame)
            sleep(0.2)
            clear_screen()
# t.me/LordDigital_LD
def print_ports_table(open_ports):
    table = PrettyTable()
    table.field_names = ["Port", "Service"]
    for port, service in open_ports.items():
        table.add_row([port, service])
    print(table)
# t.me/LordDigital_LD
if __name__ == "__main__":
    loading_animation()
    clear_screen()
    display_banner()

    while True:
        target_host = input("Enter the IP address to scan: ")
        if is_valid_ip(target_host):
            break
        else:
            print("Invalid IP address. Please enter a valid IP address.")
            clear_screen()
            display_banner()

    while True:
        try:
            start_port = int(input("Enter the starting port number: "))
            end_port = int(input("Enter the ending port number: "))
            if 0 <= start_port <= 65535 and 0 <= end_port <= 65535 and start_port <= end_port:
                ports_to_scan = list(range(start_port, end_port + 1))
                break
            else:
                print("Invalid port range. Please enter a valid range (0-65535).")
        except ValueError:
            print("Please enter valid port numbers.")

    clear_screen()
    display_banner()
    print(f"Starting port scan on {target_host} from port {start_port} to {end_port}... ")

    open_ports = scan_ports(target_host, ports_to_scan)

    output_filename = "scan_results.txt"
    write_to_file(output_filename, open_ports)
    clear_screen()
    display_banner()
    print(f"Scan results written to :: {output_filename}\n")

    print(f"Open Ports on {target_host}:")
    print_ports_table(open_ports)
