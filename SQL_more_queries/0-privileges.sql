-- My privileges!
-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

-- Attempt to display privileges for user_0d_1
SELECT 'Privileges for user_0d_1:';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Separator for clarity in output
SELECT '--------------------------------------';

-- Attempt to display privileges for user_0d_2
SELECT 'Privileges for user_0d_2:';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
