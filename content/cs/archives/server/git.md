## GIT

```bash
sudo apt install git
git config --global user.name "My Name"
git config --global user.email my@gmail.com

ssh-keygen -t ed25519 -C "my@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# copy to github
cat ~/.ssh/id_ed25519.pub # copy SSH k
```

```bash
sudo chown ubuntu /var/www
cd /var/www
git clone git@github.com:username/app.git
cd app
```