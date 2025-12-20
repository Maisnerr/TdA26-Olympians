from src.db import get_connection


def init_database():
    try:
        print("Initializing database schema...")
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        cursor.close()
        connection.close()
        print("Database schema initialized successfully!")
    except Exception as error:
        print(f"Error initializing database: {error}")
