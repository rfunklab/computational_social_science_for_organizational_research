### Introduction

This guide walk you through the steps to install MariaDB and MySQL Workbench on your Mac using Homebrew. We will also cover how to configure MariaDB to use the Aria storage engine as the default.

#### Prerequisites

- You must have macOS running on your computer.
- You should have administrative access to your machine.

#### Step 1: Installing Homebrew

Homebrew is a package manager for macOS that makes it easy to install and manage software. If you haven't installed Homebrew yet, open your Terminal and run the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

This script will walk you through the Homebrew installation process. Once installed, you'll be able to use the `brew` command to install software packages.

#### Step 2: Installing MariaDB

With Homebrew installed, you can now install MariaDB, an open-source database management system that is a compatible drop-in replacement for MySQL. To install MariaDB, run the following command in your Terminal:

```sh
brew install mariadb
```

After the installation is complete, you can start the MariaDB server with:

```sh
brew services start mariadb
```

This command will also ensure that MariaDB starts automatically at login.

#### Step 3: Configuring MariaDB to Use the Aria Storage Engine

MariaDB supports several storage engines. For computational social science projects, we recommend using the Aria storage engine for its performance benefits. To set Aria as the default storage engine, you will need to edit the MariaDB configuration file (`my.cnf`).

The `my.cnf` file may be located in different directories, depending on your installation. Typically, you can find it in `/usr/local/etc/my.cnf` or `~/.my.cnf`. If the file does not exist, you can create it in one of these locations.

Add the following lines to your `my.cnf` file:

```ini
[mysqld]
default_storage_engine=Aria
```

If you had to create the `my.cnf` file, or after you've updated it, restart MariaDB to apply the changes:

```sh
brew services restart mariadb
```

#### Step 4: Installing MySQL Workbench

MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. It provides data modeling, SQL development, and comprehensive administration tools. To install MySQL Workbench using Homebrew, run:

```sh
brew install --cask mysql-workbench
```

Once the installation is complete, you can open MySQL Workbench from your Applications folder or via Spotlight search.

#### Step 5: Connecting to MariaDB using MySQL Workbench

1. Open MySQL Workbench.
2. Click on the "+" button to add a new connection.
3. In the "Connection Name" field, you can enter any name that helps you identify the connection (e.g., "MariaDB Local").
4. For the "Connection Method", select "Standard (TCP/IP)".
5. Enter "127.0.0.1" as the Hostname and "3306" as the Port (unless you've configured MariaDB to use a different port).
6. Leave the Username as "root" and, if you've set a password during the MariaDB installation process, enter it in the Password field. You can also leave it blank if you didn't set a password.
7. Click "Test Connection" to ensure everything is set up correctly. If the test is successful, click "OK" to save the connection.

#### Conclusion

You now have MariaDB and MySQL Workbench installed and configured on your Mac using Homebrew. This setup will assist you in managing databases for your computational social science projects efficiently. 