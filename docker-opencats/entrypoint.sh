#!/bin/bash
cd /var/www/html/opencats

# Only run composer if vendor/ doesn't exist
if [ ! -d "vendor" ]; then
  echo "Running composer install for the first time..."
  composer install
else
  echo "Composer dependencies already installed."
fi

exec apache2ctl -D FOREGROUND

