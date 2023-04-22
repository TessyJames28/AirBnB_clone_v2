#!/usr/bin/env bash
# prepare web servers
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo "Hello World!" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html
echo "server {
	listen 80 default_server;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
		try_files \$uri \$uri/ =404;
	}

	error_page 404 /404.html;
	location = /404.html{
		internal;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

}" > default_file
mv -f default_file /etc/nginx/sites-enabled/default
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Hello, World ... !" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
service nginx restart
