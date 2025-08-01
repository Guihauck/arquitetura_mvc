import sqlite3

def init_db(db_path="storage.db", schema_path="init/schema.sql"):
    with open(schema_path, "r", encoding="utf-8") as file:
        schema = file.read()

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(schema)

    print("✅ Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    init_db()
