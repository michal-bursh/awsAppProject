from app import db
from app import User  # Import the User model from your app


# Initialize the database and create tables
db.create_all()
print("Database initialized and tables created.")
