import sqlite3

# Connect to SQLite
connection = sqlite3.connect("e_com.db")

# Create Cursor object for SQL execution
cursor = connection.cursor()

# Create a Table
table_info = """
CREATE TABLE e_com (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    order_quantity VARCHAR(255),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

cursor.execute(table_info)

# Insert records
cursor.execute('''INSERT INTO e_com (username, email, address, order_quantity, order_date) 
                  VALUES ('Ravi Kumar', 'ravi@example.com', '123 Street, City, India', '5', CURRENT_TIMESTAMP)''')

cursor.execute('''INSERT INTO e_com (username, email, address, order_quantity, order_date) 
                  VALUES ('Priya Sharma', 'priya@example.com', '456 Lane, City, India', '3', CURRENT_TIMESTAMP)''')

cursor.execute('''INSERT INTO e_com (username, email, address, order_quantity, order_date) 
                  VALUES ('Amit Singh', 'amit@example.com', '789 Road, City, India', '2', CURRENT_TIMESTAMP)''')

cursor.execute('''INSERT INTO e_com (username, email, address, order_quantity, order_date) 
                  VALUES ('Deepika Patel', 'deepika@example.com', '101 Avenue, City, India', '4', CURRENT_TIMESTAMP)''')

cursor.execute('''INSERT INTO e_com (username, email, address, order_quantity, order_date) 
                  VALUES ('Sandeep Gupta', 'sandeep@example.com', '202 Circle, City, India', '6', CURRENT_TIMESTAMP)''')

# Display Records
print("The inserted records are")

data = cursor.execute('''SELECT * FROM e_com''')

for row in data:
    print(row)

# Commit the transaction and close connection
connection.commit()
connection.close()
