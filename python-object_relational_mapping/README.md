# Python - Object-relational mapping

## Implemented by Xavier Cruz

## Package installed:

- Python Virtual Environment:

Although we discussed its use, it’s not clear if you've set this up. Using a virtual environment helps in managing project-specific dependencies without affecting the global Python installation.

- pkg-config:

A utility used to retrieve metadata about installed libraries. It helps in compiling applications and libraries by providing the necessary compiler and linker options.
- MariaDB Development Files (libmariadb-dev)
Development files necessary for compiling applications that connect to MariaDB, such as the mysqlclient Python library.

- mysqlclient:

A Python library that provides capabilities for connecting Python to a MySQL or MariaDB database. It’s a C extension, thus requiring the MariaDB development files and pkg-config.

- SQLAlchemy (version 2.0.31):
A powerful and flexible SQL toolkit and Object-Relational Mapping (ORM) system for Python. It abstracts database access and allows you to interact with SQL databases using Pythonic code.


- Zlib1g Development Files (zlib1g-dev): 
A compression library’s development files, which can be required for compiling software that must compress or decompress data.

## Python interpreter problems

The shebang sometime point to other interpreter
that does not have all the dependencies for that reason we need in the command line or shebang to use a specific path pointing to the enviroment that has all the depandencies

Example:

´´´bash
/path/to/your/venv/bin/python3 ./0-select_states.py root root hbtn_0e_0_usa
´´´
´´´bash
#! /path/to/your/venv/bin/python3
´´´

### Using an Enhanced Shell

MyCLI: A command line tool called mycli is designed as an enhanced MySQL/MariaDB client that supports auto-completion and syntax highlighting. 

- You can install it using pip:
´´´bash
pip install mycli
´´´
- Connect to your MariaDB database with:
´´´bash
mycli -u root -p Your_password_for_mariadb
´´´

### Change password of your Mariadb

Step 1
´´´bash
mysql -u root -p
´´´
Step 2
´´´bash
ALTER USER 'root'@'localhost' IDENTIFIED BY 'mynewpassword';
´´´
Step 3
´´´bash
FLUSH PRIVILEGES;

Step 4
EXIT;
´´´