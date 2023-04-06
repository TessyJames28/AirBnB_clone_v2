#!/usr/bin/env bash
# Bash script that sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir -p /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared
mkdir /data/web_static/releases/test
SET_FILE="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$SET_FILE" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "server {
        listen 80 default_server;

        root /var/www/html;
        index index.html;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}

        location /redirect_me {
                return 301 https://www.digitalocean.com/community/;
        }

        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html;
                internal;
        }
}" > default_file
sudo mv -f default_file /etc/nginx/sites-enabled/default
service nginx restart
