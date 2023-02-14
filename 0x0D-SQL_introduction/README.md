<h1>0x0D. SQL - Introduction</h1>
<code>SQL</code> <code>MySQL</code>
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt="" loading="lazy" style="">

<h2>Learning Objectives</h2>
<h3>General</h3>

1. What is a database?
2. What is a relational database?
3. What does SQL stand for
4. What’s MySQL
5. How to create a database in MySQL
6. What does DDL and DML stand for
7. How to CREATE or ALTER a table
8. How to SELECT data from a table
9. How to INSERT, UPDATE or DELETE data
10. What are subqueries
11. How to use MySQL functions

<h2>More Info</h2>
<h3>Comments for your SQL file</h3>


```bash, sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```


<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>


```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```


Connect to your MYSql Server:


```bash, sql
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```


<h2>Use "container-on-demand" to run MySQL</h2>
<h3>In the container, the credentials are <code>root/root</code></h3>

1. Ask for container Ubuntu 20.04
2. Connect via SSH
3. OR connect via the Web terminal
4. In the container, you should start MySQL before playing with it:


```bash, sql
$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```
