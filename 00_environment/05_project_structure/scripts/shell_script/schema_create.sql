CREATE database icesi_blog;
USE icesi_blog;
CREATE TABLE user(
id INT NOT NULL AUTO_INCREMENT, 
PRIMARY KEY(id),
 username VARCHAR(80),
 email VARCHAR(120));
INSERT INTO user (username,email) VALUES ('flanders','flanders@springfield.com');
INSERT INTO user (username,email) VALUES ('homero','homero@springfield.com');
-- http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch34_:_Basic_MySQL_Configuration
GRANT ALL PRIVILEGES ON icesi_blog.* to 'icesi-admin'@'localhost' IDENTIFIED by 'icesiblogpassword';