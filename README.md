# Setting Up PostgreSQL Database for Your Project

## Step 1 — Installing PostgreSQL

To install PostgreSQL, first refresh your server’s local package index:

```bash
sudo apt update
```
Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality:

```bash
sudo apt install postgresql postgresql-contrib
```

Ensure that the service is started:

```bash
sudo systemctl start postgresql.service
```

## Step 2 — Using PostgreSQL

First create database 

```bash
create database database_name
```
