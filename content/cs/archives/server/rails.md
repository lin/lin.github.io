## Rails -v

### 1. RVM -v

Exactly based on [https://github.com/rvm/ubuntu_rvm]()

```bash
sudo apt-get install software-properties-common
sudo apt-add-repository -y ppa:rael-gc/rvm
sudo apt update
```

```bash
sudo apt-get install rvm
sudo usermod -a -G rvm $USER
echo 'source "/etc/profile.d/rvm.sh"' >> ~/.bashrc
exit
su ubuntu
```

### 2. RUBY -v

```bash
rvm install "ruby-3.3.0"
ruby -v
```

### 3. RAILS -v

```bash
gem install rails -v '7.0.8' -V --no-document
rails -v
gem sources --remove https://rubygems.org/
gem sources -a https://gems.ruby-china.com
```

### 4. NODE -v

```bash
sudo apt install nodejs
node -v
sudo apt install npm
sudo npm install -g yarn

# if want newest stable version
sudo npm cache clean -f
sudo npm install -g n
sudo n stable

npm config set registry https://registry.npmmirror.com
yarn config set registry https://registry.npmmirror.com
```

### 5. test rails

```bash
rails new blog --css=tailwind --javascript=esbuild --database=postgresql
rails db:create
bin/dev # 3000
```

```bash
rails generate controller HelloWorld
# controller
class HelloWorldController < ApplicationController
  def greet
    render plain: 'Hello, World!'
  end
end
# routes
root "hello_world#greet"
```