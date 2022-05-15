sudo mysql -u root --execute="CREATE DATABASE wordpressdb;"
sudo mysql -u root --execute="CREATE USER 'wordpress_ysanta'@'localhost' identified by 'wordpress123';"
sudo mysql -u root --execute="GRANT ALL PRIVILEGES ON wordpressdb.* TO 'wordpress_ysanta'@'localhost'"

