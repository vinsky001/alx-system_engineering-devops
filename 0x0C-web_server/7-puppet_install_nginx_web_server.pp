#!/usr/bin/env bash
# Install Nginx package

package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "
    server {
      listen 80;
      root /var/www/html;
      index index.html;
      location / {
        try_files $uri $uri/ =404;
      }
      location /redirect_me {
        return 301 https://www.example.com/;
      }
    }
  ",
  notify => Service['nginx'],
}

# Create root page
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Enable Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
