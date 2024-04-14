#!/usr/bin/env bash

# Update package lists, upgrade packages, and install Nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create necessary directories and files
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Welcome to My Server" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to set up the current version
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories to user and group
sudo chown -hR ubuntu:ubuntu /data/

# Configure Nginx to serve static files
new_location="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "45i $new_location" /etc/nginx/sites-available/default

# Start, restart, and reload Nginx service
sudo service nginx start
sudo service nginx restart
sudo service nginx reload
