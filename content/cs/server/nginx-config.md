### Config


```bash
passenger-config about ruby-command
# passenger_ruby /usr/share/rvm/gems/ruby-3.3.0/wrappers/ruby
```


```bash
sudo vim /etc/nginx/nginx.conf
```

```bash
server {
    listen 80;
    server_name 1.2.3.4;

    root /var/www/app/public;

    passenger_enabled on;
    passenger_ruby /usr/share/rvm/gems/ruby-3.3.0/wrappers/ruby;
}
```

```bash
sudo service nginx reload
sudo service nginx restart

passenger-status
sudo passenger-config restart-app $(pwd)
```