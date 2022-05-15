sudo mysql -u root --execute="CREATE DATABASE icehrmdb;"
sudo mysql -u root --execute="CREATE USER 'icehrm_ysanta'@'localhost' identified by 'icehrm_pwd';"
sudo mysql -u root --execute="GRANT ALL PRIVILEGES ON icehrmdb.* TO 'icehrm_ysanta'@'localhost'"

