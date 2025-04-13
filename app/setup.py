from app.db_create import createAll
from app.seed_data import seed_database

if __name__ == "__main__":
  print(createAll())
  print(seed_database())
