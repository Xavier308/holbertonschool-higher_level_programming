-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Select the database for use
USE hbtn_0e_0_usa;

-- Create the table 'states' if it doesn't already exist
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data into the table
INSERT INTO states (name) VALUES 
('California'), 
('Arizona'), 
('Texas'), 
('New York'), 
('Nevada');
