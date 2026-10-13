## PG

```bash
sudo apt install postgresql postgresql-contrib
psql --version
```

### User

```bash
# sudo -u postgres psql postgres 
sudo -i -u postgres
psql postgres
\password postgres
\q

# sudo -u postgres createuser --superuser ubuntu
createuser --superuser ubuntu
sudo -u postgres psql postgres
\password ubuntu
\q
```

```bash
sudo /etc/init.d/postgresql start
# pg_ctl -D /usr/local/var/postgres start
sudo /etc/init.d/postgresql restart
sudo /etc/init.d/postgresql stop
```

### Commands

Backslash

1. \l : list all dbs
1. \c : connect to a db
1. \du : list all user
1. \d : list all tables
1. \d <table_name>: list 

Backup and restore

1. pg_dump <database_name> > backup.sql
1. pg_restore -d <database_name> backup.sql