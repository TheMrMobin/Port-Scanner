#!/bin/bash

# Display banner function
display_banner() {
  clear
  banner="
===============================================================================   
 ____            _     ____                                   __     ______
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __  \ \   / /___ \\
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  \ \ / /  __) |
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |      \ V /  / __/
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|       \_/  |_____|


                         Telegram: @LordDigitdl_LD
===============================================================================
"
  echo "$banner"
}

# Show banner at the start
display_banner

# Update package list
echo "Updating package list..."
sudo apt-get update
# Clear screen and display banner
display_banner

# Install Python3 and pip if not installed
echo "Installing Python3 and pip if they are not already installed..."
sudo apt-get install -y python3 python3-pip
# Clear screen and display banner
display_banner

# Install PrettyTable and tqdm using pip
echo "Installing required Python packages (prettytable and tqdm)..."
pip3 install prettytable tqdm
# Clear screen and display banner
display_banner

# Find the directory containing PortScannerV2.py
SCRIPT_DIR=$(dirname "$(realpath PortScannerV2.py)")

# Make PortScannerV2.py executable
echo "Making PortScannerV2.py executable..."
chmod +x "$SCRIPT_DIR/PortScannerV2.py"
# Clear screen and display banner
display_banner

# Navigate to the directory containing PortScannerV2.py
echo "Navigating to $SCRIPT_DIR ..."
cd "$SCRIPT_DIR"
# Clear screen and display banner
display_banner

# Run PortScannerV2.py
echo "Running PortScannerV2.py ..."
python3 PortScannerV2.py
