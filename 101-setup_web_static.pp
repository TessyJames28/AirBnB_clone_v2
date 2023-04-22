# Configure web server

$server_conf = "server {
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
}"

$command_list = "echo '${server_conf}' > /etc/nginx/sites-enabled/default ;
mkdir -p /data/web_static/shared/ ; 
mkdir -p /data/web_static/releases/test/ ; 
echo 'Hello, World ... !' | tee /data/web_static/releases/test/index.html ;
ln -sf /data/web_static/releases/test/ /data/web_static/current ; 
chown -R ubuntu:ubuntu /data ; 
service nginx restart"

exec { 'nginx':
  command  => 'sudo apt -y update && sudo apt -y install nginx',
  provider => 'shell'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello, World!',
  require => Exec['nginx']
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Exec['nginx']
}

exec { 'write_server':
  command  => $command_list,
  provider => 'shell',
  require  => File['/var/www/html/404.html']
}
