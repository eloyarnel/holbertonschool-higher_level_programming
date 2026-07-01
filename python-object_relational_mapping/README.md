# SQL - ORM

## Description

This project introduces the use of Object Relational Mapping (ORM) in Python using SQLAlchemy. The goal is to interact with a MySQL database through Python objects instead of writing raw SQL queries. ORM allows developers to map database tables to Python classes and manipulate data using Python code.

Throughout the project, Python scripts are used to query, insert, update, and delete records from a database while maintaining secure and structured database interactions.

## Learning Objectives

By the end of this project, you should be able to explain:

* What Object Relational Mapping (ORM) is
* How to connect Python to a MySQL database
* How to use SQLAlchemy to interact with databases
* How to create and manage sessions
* How to perform CRUD operations using ORM
* How to prevent SQL injections
* The difference between raw SQL queries and ORM queries

## Requirements

* Ubuntu 20.04 LTS
* Python 3.8+
* MySQL 8.0
* SQLAlchemy 1.4.x
* mysqlclient 2.0.x
* All Python scripts must start with `#!/usr/bin/python3`
* All files must end with a new line

## Installation

Install the required dependencies:

```bash
sudo apt-get update
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
sudo pip3 install SQLAlchemy==1.4.22
```

Verify installation:

```bash
python3
```

```python
import MySQLdb
import sqlalchemy
print(MySQLdb.version_info)
print(sqlalchemy.__version__)
```

## Usage

Each script connects to a MySQL database using command line arguments:

```bash
./script.py <mysql_username> <mysql_password> <database_name>
```

Example:

```bash
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
```

## Example Output

```
1: California
2: Arizona
3: Texas
```

## Main Concepts Used

* Python classes
* SQLAlchemy ORM
* Database sessions
* Query filtering
* Object creation and persistence
* Secure database interactions

## Author

Eloy A. Alicea Sanchez
