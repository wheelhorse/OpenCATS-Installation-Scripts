#!/bin/sh
# This script will install a new OpenCATS instance on a fresh Ubuntu 18.04 server.
# This script is experimental and does not ensure any security.


export DEBIAN_FRONTEND=noninteractive
apt update
add-apt-repository -y ppa:ondrej/php
apt update
apt upgrade -y
apt install -y mariadb-server mariadb-client apache2 php7.1 php7.1-soap php7.1-ldap php7.1-mysql php7.1-gd php7.1-xml php7.1-curl php7.1-mbstring php7.1-zip php7.1-json antiword poppler-utils html2text unrtf

# Set up database
sudo mysql -u root --execute="CREATE DATABASE cats_dev;"
sudo mysql -u root --execute="CREATE USER 'cats'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -u root --execute="GRANT ALL PRIVILEGES ON cats_dev.* TO 'cats'@'localhost';"

# Download OpenCATS
cd /var/www/html
wget https://github.com/opencats/OpenCATS/archive/0.9.5-3.zip
unzip 0.9.5-3.zip
mv /var/www/html/OpenCATS-0.9.5-3 opencats

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
php5.6 php5.6-soap php5.6-ldap php5.6-mysql php5.6-gd php5.6-xml php5.6-curl php5.6-mbstring php5.6-zip
