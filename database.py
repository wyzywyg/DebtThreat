#database.py

import pymysql
class Database:

    def __init__(self):
        self.host = "localhost"
        self.user = "jaron"
        self.password = "admin"
        self.database = "debt_threat"
        self.current_user = None
        self.db = None
        self.cursor = None
        self.connect_to_database()
        self.initialize_users_table()

    def connect_to_database(self):
        """Connect to the database or create one if it doesn't exist."""
        try:
            self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
            )
            self.cursor = self.db.cursor()   
        except pymysql.OperationalError as e:
            if e.args[0] == 1049:  # MySQL error code 1049 corresponds to "Unknown database"
                self.create_database()
                # Reconnect to the newly created database
                self.db = pymysql.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                self.cursor = self.db.cursor()
            else:
                raise  # Re-raise the exception for other operational errors

    def create_database(self):
        """Create the database if it doesn't exist."""
        self.db = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password
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
            
    def initialize_users_table(self):
        """Create the 'users' table if it doesn't exist and also create related tables."""
        try:
            # Create the 'users' table if it doesn't exist
            create_users_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                final_score INT
            )
            """
            self.cursor.execute(create_users_table_query)
            print("Table 'users' created successfully.")

            # Create the 'player_info' table if it doesn't exist
            create_player_info_table_query = """
            CREATE TABLE IF NOT EXISTS player_info (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                player_name VARCHAR(255),
                difficulty VARCHAR(255),
                university_type VARCHAR(255),
                program VARCHAR(255),
                dorm_type VARCHAR(255),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
            """
            self.cursor.execute(create_player_info_table_query)
            print("Table 'player_info' created successfully.")

            # Create the 'user_stats' table if it doesn't exist
            create_user_stats_table_query = """
            CREATE TABLE IF NOT EXISTS user_stats (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                debt INT,
                debt_money INT,
                education INT,
                health INT,
                happiness INT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
            """
            self.cursor.execute(create_user_stats_table_query)
            print("Table 'user_stats' created successfully.")

            # Commit the changes
            self.db.commit()

        except pymysql.Error as e:
            print(f"Error creating tables: {e}")
            self.db.rollback()  # Rollback the changes in case of an error
            raise  # Re-raise the exception to see the full error details
            
    def save_user_data(self, player_name, final_score, difficulty, university_type, program, dorm_type,
                       debt, debt_money, education, health, happiness):
        """Save user data in 'users', 'player_info', and 'user_stats' tables."""
        try:
            # Insert the username and final score into the 'users' table
            insert_user_query = "INSERT INTO users (username, final_score) VALUES (%s, %s)"
            self.cursor.execute(insert_user_query, (player_name, final_score))
            user_id = self.cursor.lastrowid  # Get the last inserted user_id (primary key)

            # Insert player info into 'player_info' table using the user_id as a foreign key
            insert_player_info_query = (
                "INSERT INTO player_info (user_id, player_name, difficulty, university_type, program, dorm_type) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            self.cursor.execute(insert_player_info_query, (user_id, player_name, difficulty, university_type,
                                                           program, dorm_type))

            # Insert user stats into 'user_stats' table using the user_id as a foreign key
            insert_user_stats_query = (
                "INSERT INTO user_stats (user_id, debt, debt_money, education, health, happiness) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            self.cursor.execute(insert_user_stats_query, (user_id, debt, debt_money, education, health, happiness))

            self.db.commit()  # Commit the changes to the database

        except pymysql.Error as e:
            self.db.rollback()  # Rollback the changes in case of an error
            print(f"Error saving user data: {e}")

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
