# Dockerfile for OpenCATS with volume support
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt update && \
    apt upgrade -y && \
    apt install -y mariadb-client apache2 php7.4 php7.4-cli php7.4-fpm php7.4-common \
                   php7.4-soap php7.4-ldap php7.4-mysql php7.4-gd php7.4-xml php7.4-curl \
                   php7.4-mbstring php7.4-zip php7.4-json antiword poppler-utils html2text \
                   unrtf wget unzip composer && \
    rm -rf /var/lib/apt/lists/*

# Create web root directory
RUN mkdir -p /var/www/html/opencats

# Set permissions (will apply to mounted content too)
RUN chown www-data:www-data -R /var/www/html && \
    chmod -R 770 /var/www/html

# Expose Apache port
EXPOSE 80
EXPOSE 443

# Start Apache in the foreground
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

