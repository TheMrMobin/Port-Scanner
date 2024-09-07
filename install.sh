#!/bin/bash

# Display banner function

  clear


# Show banner at the start


# Define variables
REPO_URL="https://github.com/TheMrMobin/Port-Scanner/archive/refs/heads/main.zip"
DOWNLOAD_DIR="PortScanner"
ZIP_FILE="PortScanner.zip"

# Update package list
echo "Updating package list..."
sudo apt-get update
# Clear screen and display banner


# Install required packages
echo "Installing required packages (unzip, Python3, pip)..."
sudo apt-get install -y unzip python3 python3-pip
# Clear screen and display banner


# Create download directory
echo "Creating directory $DOWNLOAD_DIR ..."
mkdir -p "$DOWNLOAD_DIR"
# Clear screen and display banner


# Download the zip file
echo "Downloading zip file from $REPO_URL..."
curl -L -o "$DOWNLOAD_DIR/$ZIP_FILE" "$REPO_URL"
# Clear screen and display banner


# Unzip the file
echo "Unzipping $ZIP_FILE ..."
unzip "$DOWNLOAD_DIR/$ZIP_FILE" -d "$DOWNLOAD_DIR"
# Clear screen and display banner


# Find the directory containing PortScannerV2.py
SCRIPT_DIR=$(find "$DOWNLOAD_DIR" -type d -name 'Port-Scanner-main')

# Install Python packages from requirements.txt if exists
if [ -f "$SCRIPT_DIR/requirements.txt" ]; then
    echo "Installing Python packages from requirements.txt..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
fi

# Make PortScannerV2.py executable
echo "Making PortScannerV2.py executable..."
chmod +x "$SCRIPT_DIR/PortScannerV2.py"
# Clear screen and display banner


# Navigate to the directory containing PortScannerV2.py
echo "Navigating to $SCRIPT_DIR ..."
cd "$SCRIPT_DIR"
# Clear screen and display banner


# Run PortScannerV2.py
echo "Running PortScannerV2.py ..."
python3 PortScannerV2.py
