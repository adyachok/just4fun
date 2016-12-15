CREATE DATABASE dezi;

CREATE USER 'dezi'@'localhost' IDENTIFIED BY 'dezi';
GRANT ALL PRIVILEGES ON dezi.* TO 'dezi'@'localhost';
FLUSH PRIVILEGES;