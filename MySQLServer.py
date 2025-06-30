import mysql.connector
from mysql.connector import errorcode

def create_database():
    # MySQL server connection parameters
    host = 'localhost'  # or your MySQL server address
    user = 'root'  # your MySQL username
    password = 'your_password'  # your MySQL password

    # Try to connect to the MySQL server
    try:
        # Establishing the connection
        connection = mysql.connector.connect(host=host, user=user, password=password)
        
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Commit the transaction
        connection.commit()
        
        # Print success message
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        # Print error message if connection fails
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)
    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
if __name__ == "__main__":
    create_database()