## Production 


### Initial

```bash
sudo apt install libpq-dev
bundle install
EDITOR="vim --wait" bin/rails credentials:edit # copy content in master.key to server
```

```bash
# change username in database.yml
RAILS_ENV=production rake db:create
RAILS_ENV=production rake db:migrate
RAILS_ENV=production rake db:seed

RAILS_ENV=production rake assets:precompile
```