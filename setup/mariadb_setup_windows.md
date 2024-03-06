### Introduction

This guide provides step-by-step instructions on how to install MariaDB and MySQL Workbench on a Windows system. Additionally, we'll cover configuring MariaDB to use the Aria storage engine as the default, enhancing your database management capabilities.

#### Prerequisites

- Ensure you have a Windows operating system running on your computer.
- Administrative access to your machine is required for installation.

#### Step 1: Installing MariaDB

MariaDB is a robust, scalable, and reliable SQL server that is a drop-in replacement for MySQL. To install MariaDB on Windows:

1. **Download MariaDB**: Go to the official MariaDB [download page](https://mariadb.org/download/) and choose the version suitable for Windows. Download the `.msi` installer file.
2. **Run the Installer**: Double-click on the downloaded `.msi` file to start the installation process. Follow the on-screen instructions.
   - When prompted, select a root password for MariaDB. Remember this password, as you'll need it to manage databases.
   - Ensure the "Enable access from remote machines for 'root' user" option is unchecked for security reasons unless required for your project.
   - Check the "Use UTF8 as default server’s character set" option for better compatibility.
3. **Complete the Installation**: Continue following the prompts, selecting your preferences for installation. Once the installation is complete, MariaDB will be available on your system.

#### Step 2: Configuring MariaDB to Use the Aria Storage Engine

To optimize performance for computational social science projects, we recommend setting the Aria storage engine as the default for MariaDB:

1. **Locate the `my.ini` File**: After installation, find the `my.ini` file in the MariaDB installation directory, typically located in `C:\Program Files\MariaDB 10.x\` (where "10.x" corresponds to the version you installed).
2. **Edit the `my.ini` File**: Open the `my.ini` file with a text editor like Notepad as an administrator. Under the `[mysqld]` section, add the following line:
   ```ini
   default_storage_engine=Aria
   ```
3. **Restart MariaDB**: For the changes to take effect, restart the MariaDB service. You can do this by opening the Services app, finding the MariaDB service, and clicking on "Restart".

#### Step 3: Installing MySQL Workbench

MySQL Workbench is a comprehensive tool for database management and development. Here's how to install it on Windows:

1. **Download MySQL Workbench**: Visit the official MySQL Workbench [download page](https://dev.mysql.com/downloads/workbench/) and select the Windows version.
2. **Run the Installer**: Double-click the downloaded `.msi` file and follow the on-screen instructions to install MySQL Workbench. Choose the default settings for a straightforward installation.

#### Step 4: Connecting to MariaDB using MySQL Workbench

1. Open MySQL Workbench.
2. In the home screen, click on the "+" icon next to "MySQL Connections" to set up a new connection.
3. Name the connection (e.g., "MariaDB Local") in the "Connection Name" field for easy identification.
4. For "Connection Method", keep the default "Standard (TCP/IP)".
5. Enter "127.0.0.1" as the Hostname and "3306" as the Port unless you've customized MariaDB's port.
6. The Username is "root" by default. Enter the root password you set during the MariaDB installation process in the Password field.
7. Click "Test Connection" to ensure everything is correctly set up. If the connection is successful, click "OK" to save it.

#### Conclusion

You now have MariaDB and MySQL Workbench installed and properly configured on your Windows system, with the Aria storage engine set as the default for enhanced performance. This environment will support your computational social science projects by providing a robust platform for database management and analysis.