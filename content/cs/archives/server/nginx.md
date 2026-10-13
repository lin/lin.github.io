## Nginx

```bash
# installation
sudo apt install nginx
nginx -v 
sudo service nginx start
sudo service nginx stop
```

```bash
# How to use ngnix
vim /etc/nginx/nginx.conf # nginx config file location
sudo nginx -s reload # make config file working
```

### Passenger

[https://www.phusionpassenger.com/docs/advanced_guides/install_and_upgrade/nginx/install/oss/jammy.html]()

```bash
sudo apt-get install -y dirmngr gnupg apt-transport-https ca-certificates curl
curl https://oss-binaries.phusionpassenger.com/auto-software-signing-gpg-key.txt | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/phusion.gpg >/dev/null

# Add our APT repository
sudo sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger jammy main > /etc/apt/sources.list.d/passenger.list'
sudo apt-get update

# Install Passenger + Nginx module
sudo apt-get install -y libnginx-mod-http-passenger
if [ ! -f /etc/nginx/modules-enabled/50-mod-http-passenger.conf ]; then sudo ln -s /usr/share/nginx/modules-available/mod-http-passenger.load /etc/nginx/modules-enabled/50-mod-http-passenger.conf ; fi
sudo ls /etc/nginx/conf.d/mod-http-passenger.conf
sudo /usr/bin/passenger-config validate-install
```