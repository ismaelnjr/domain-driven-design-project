from database.orm.models import init_db


def migrate(db_path: str):
    print("Iniciando a migração do banco de dados...")
    engine = init_db(db_path)
    print("Tabelas criadas ou atualizadas com sucesso!")
    return engine