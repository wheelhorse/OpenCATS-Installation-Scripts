#!/bin/sh
# This script will install a new OpenCATS instance on a fresh Ubuntu 18.04 server.
# This script is experimental and does not ensure any security.
# This script is for ubuntu 20.04 TSL


export DEBIAN_FRONTEND=noninteractive
apt update
apt upgrade -y
apt install -y mariadb-server mariadb-client apache2 php php-cli php-fpm php-common php-soap php-ldap php-mysql php-gd php-xml php-curl php-mbstring php-zip php-json php-pear php-bcmath antiword poppler-utils html2text unrtf

# Set up database
sudo mysql -u root --execute="CREATE DATABASE cats_dev;"
sudo mysql -u root --execute="CREATE USER 'cats'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -u root --execute="GRANT ALL PRIVILEGES ON cats_dev.* TO 'cats'@'localhost';"

# Download OpenCATS
cd /var/www/html
https://github.com/opencats/OpenCATS/releases/download/0.9.6/opencats-0.9.6-full.zip
unzip opencats-0.9.6-full.zip
mv /var/www/html/opencats-0.9.6-full opencats

# Install composer
apt install -y composer
cd /var/www/html/opencats

# Install OpenCATS composer dependancies
composer install
cd ..

# Set file and folder permissions
chown www-data:www-data -R opencats && chmod -R 770 opencats/attachments opencats/upload

# Restart Apache to load new config
service apache2 restart

echo ""
echo "Setup Finished, Your OpenCATS applicant tracking system should now be installed."
echo "MySQL was installed without a root password, It is recommended that you set a root MySQL password."
echo ""

echo "You can finish installation of your OpenCATS applicant tracking system at: http://localhost/opencats"
