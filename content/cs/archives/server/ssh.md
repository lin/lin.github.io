## SSH (Secure Shell)

### Create a new user

```bash
# create the user
sudo adduser ubuntu 

# User Modification, --append, --Group add ubuntu to sudo group
# sudo means superuser do
usermod -a -G sudo ubuntu

# switch user
su ubuntu
```

### Generate key-pair

```bash
# generate 
# id_rsa is private, id_rsa.pub
# RSA is Rivest-Shamir-Adleman, the name of the algorithm
ssh-keygen

# authorize the public key
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# display private key, so you can copy this to your local computer
# remember to add a newline at the end of the file
cat ~/.ssh/id_rsa
```

### Change pem file mode

Private key should have permission 0600 while your public key have permission 0644.

```bash
# at your local computer
# remember to add a newline at the end of the file for pem
chmod 0600 ~/.ssh/app.pem
```

#### Disable Password Auth

```bash
sudo vim /etc/ssh/sshd_config

# set these to no
KbdInteractiveAuthentication no
PasswordAuthentication no

# restart ssh
sudo systemctl restart ssh
```