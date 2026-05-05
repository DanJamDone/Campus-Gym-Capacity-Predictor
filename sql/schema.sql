-- Create the database
CREATE DATABASE rutgers_gym_db;
USE rutgers_gym_db;

-- This table stores each unique gym
CREATE TABLE gyms (
    gym_id INT AUTO_INCREMENT PRIMARY KEY,
    gym_name VARCHAR(100) NOT NULL UNIQUE
);

-- This tables stores busyness readings for each gym
CREATE TABLE popular_times (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gym_id INT NOT NULL,
    day_of_week VARCHAR(10) NOT NULL,
    hour VARCHAR(10) NOT NULL,
    hour_24 INT,
    is_weekend TINYINT(1),
    busyness_pct, INT NOT NULL,
    capacity_label VARCHAR(10),
    FOREIGN KEY(gym_id) REFERENCES gyms(gym_id)
);

