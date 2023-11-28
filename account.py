import pymysql

class Account:

    def __init__(self):
        self.current_user = None
        self.db = None
        self.cursor = None
        self.connect_to_database()
        self.create_users_table()

    def connect_to_database(self):
        """Connect to the database or create one if it doesn't exist."""
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="jaron",
                password="admin",
                database="debt_threat"  # Use the correct database name
            )
            self.cursor = self.db.cursor()
        except pymysql.OperationalError as e:
            if e.args[0] == 1049:  # MySQL error code 1049 corresponds to "Unknown database"
                self.create_database()
                # Reconnect to the newly created database
                self.db = pymysql.connect(
                    host="localhost",
                    user="jaron",
                    password="admin",
                    database="debt_threat"  # Use the correct database name
                )
                self.cursor = self.db.cursor()
            else:
                raise  # Re-raise the exception for other operational errors

    def create_database(self):
        """Create the database if it doesn't exist."""
        self.db = pymysql.connect(
            host="localhost",
            user="jaron",
            password="admin"
        )
        self.cursor = self.db.cursor()
        create_database_query = "CREATE DATABASE IF NOT EXISTS debt_threat"  # Use the correct database name

        try:
            self.cursor.execute(create_database_query)

            # Grant privileges on the database to the user 'jaron'
            grant_privileges_query = "GRANT ALL PRIVILEGES ON debt_threat.* TO 'jaron'@'localhost'"
            self.cursor.execute(grant_privileges_query)

            # Commit the changes
            self.db.commit()

            self.cursor.close()  # Close the cursor after creating the database
            print("Database created successfully.")
        except pymysql.Error as e:
            print(f"Error creating database: {e}")
            raise  # Re-raise the exception to see the full error details

    def create_users_table(self):
        """Create the 'users' table if it doesn't exist."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            final_score INT
        )
        """
        try:
            self.cursor.execute(create_table_query)
            print("Table 'users' created successfully.")
        except pymysql.Error as e:
            print(f"Error creating 'users' table: {e}")
            raise  # Re-raise the exception to see the full error details

    def save_name(self, username):
        """Save a user's username in the 'users' table."""
        try:
            # Insert the username into the 'users' table
            insert_query = "INSERT INTO users (username) VALUES (%s)"
            self.cursor.execute(insert_query, (username,))
            self.db.commit()  # Commit the changes to the database

        except pymysql.Error as e:
            self.db.rollback()  # Rollback the changes in case of an error
            print(f"Error saving user: {e}")

    def save_final_score(self, final_score):
        """Save a user's final score in the 'users' table."""
        try:
            # Insert the final score into the 'users' table
            insert_query = "INSERT INTO users (final_score) VALUES (%s)"
            self.cursor.execute(insert_query, (final_score,))
            self.db.commit()  # Commit the changes to the database

        except pymysql.Error as e:
            self.db.rollback()  # Rollback the changes in case of an error
            print(f"Error saving final score: {e}")

    def fetch_leaderboard_data(self):
        """Fetch leaderboard data from the 'users' table."""
        try:
            # Select usernames and final scores from the 'users' table
            query = "SELECT username, final_score FROM users ORDER BY final_score DESC"
            self.cursor.execute(query)

            # Fetch all the rows as a list of tuples
            rows = self.cursor.fetchall()

            # Convert the list of tuples to a list of dictionaries
            leaderboard_data = [{'username': row[0], 'final_score': row[1]} for row in rows]

            return leaderboard_data

        except pymysql.Error as e:
            print(f"Error fetching leaderboard data: {e}")
