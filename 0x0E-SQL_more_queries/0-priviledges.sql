-- Script that lists all privileges of the MySQL users
-- Query to list all privileges (GRANT) of the MySQL users
SELECT * FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';

