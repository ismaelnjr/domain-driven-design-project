from database.database import migrate

DATABASE = "carros.db"

if __name__ == "__main__":
    migrate(DATABASE)