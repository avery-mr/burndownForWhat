from app.db_create import createAll
from app.seed_data import seed_database

if __name__ == "__main__":
    try:
        print("Creating database tables...")
        print(createAll())
        print("Seeding database...")
        print(seed_database())
    except Exception as e:
        print(f"Setup failed: {str(e)}")
        raise
