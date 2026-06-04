CREATE DATABASE IF NOT EXISTS bluebird_hotel; 
USE bluebird_hotel; -- ========================= -- Admin Login Table -- ========================= 
CREATE TABLE IF NOT EXISTS admin ( 
    admin_id VARCHAR(50) PRIMARY KEY, 
   
  password VARCHAR(100) NOT NULL 
); 
INSERT INTO admin (admin_id, password) 
VALUES ('admin', 'admin123') 
ON DUPLICATE KEY UPDATE password='admin123'; -- ========================= -- Rooms Table -- ========================= 
CREATE TABLE IF NOT EXISTS rooms ( 
    room_id INT AUTO_INCREMENT PRIMARY KEY, 
    room_number VARCHAR(20) NOT NULL UNIQUE, 
    room_type VARCHAR(50) NOT NULL, 
    price DECIMAL(10,2) NOT NULL, 
    status VARCHAR(20) DEFAULT 'Available' 
); -- ========================= -- Reservations Table -- ========================= 
CREATE TABLE IF NOT EXISTS reservations ( 
    reservation_id INT AUTO_INCREMENT PRIMARY KEY, 
    customer_name VARCHAR(100) NOT NULL, 
    email VARCHAR(100), 
    phone VARCHAR(20), 
    room_number VARCHAR(20), 
    check_in DATE, 
    check_out DATE, 
    guests INT DEFAULT 1, 
    meal_plan VARCHAR(50), 
    booking_status VARCHAR(20) DEFAULT 'Reserved' 
); -- ========================= -- Bookings Table -- ========================= 
CREATE TABLE IF NOT EXISTS bookings ( 
    booking_id INT AUTO_INCREMENT PRIMARY KEY, 
    customer_name VARCHAR(100) NOT NULL, 
    email VARCHAR(100), 
    phone VARCHAR(20), 
    room_number VARCHAR(20), 
    room_type VARCHAR(50), 
    check_in DATE, 
    check_out DATE, 
    total_amount DECIMAL(10,2), 
    payment_status VARCHAR(20) DEFAULT 'Pending'); -- ========================= -- Billing Table -- ========================= 
CREATE TABLE IF NOT EXISTS billing ( 
    bill_id INT AUTO_INCREMENT PRIMARY KEY, 
  booking_id INT, 
    customer_name VARCHAR(100), 
    room_charges DECIMAL(10,2), 
    food_charges DECIMAL(10,2), 
    tax DECIMAL(10,2),  
  total_amount DECIMAL(10,2), 
    bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); -- ========================= -- Checkout Table -- ========================= 
CREATE TABLE IF NOT EXISTS checkout ( 
    checkout_id INT AUTO_INCREMENT PRIMARY KEY, 
    booking_id INT, 
    customer_name VARCHAR(100), 
    room_number VARCHAR(20), 
    checkout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    total_paid DECIMAL(10,2), 
    remarks VARCHAR(255)); 
