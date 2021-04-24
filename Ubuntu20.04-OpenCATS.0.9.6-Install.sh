#!/bin/sh
# This script will install a new OpenCATS instance on a fresh Ubuntu 18.04 server.
# This script is experimental and does not ensure any security.
# This script is for ubuntu 20.04 TSL


export DEBIAN_FRONTEND=noninteractive
apt update
apt upgrade -y
apt install -y mariadb-server mariadb-client apache2 php7.4 php7.4-cli php7.4-fpm php7.4-common php7.4-soap php7.4-ldap php7.4-mysql php7.4-gd php7.4-xml php7.4-curl php7.4-mbstring php7.4-zip php7.4-json antiword poppler-utils html2text unrtf

# Set up database
sudo mysql -u root --execute="CREATE DATABASE cats_dev;"
sudo mysql -u root --execute="CREATE USER 'cats'@'localhost' IDENTIFIED BY 'password';"
sudo mysql -u root --execute="GRANT ALL PRIVILEGES ON cats_dev.* TO 'cats'@'localhost';"

cd /var/www/html
# Download OpenCATS
wget https://github.com/wheelhorse/OpenCATS/archive/refs/heads/ysanta-096.zip
unzip ysanta-096.zip
mv /var/www/html/OpenCATS-ysanta-096 opencats

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
