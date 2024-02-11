
from cookiecutter.main import cookiecutter
from dotenv import set_key

project_template = "{{cookiecutter.project_name}}"

# Pergunta ao usuário
connect_to_database = input("Deseja se conectar a algum banco de dados? (yes/no): ")

# Caso o usuário deseje se conectar a um banco de dados
if connect_to_database.lower() in ["yes", "y", "true"]:
    database_type = input("Se sim, selecione o tipo de banco de dados (MySQL/PostgreSQL/SQLite/Outro): ")
    database_user = input("Usuário do banco de dados: ")
    database_password = input("Senha do banco de dados: ")
    database_host = input("Host do banco de dados: ")
    database_name = input("Nome do banco de dados: ")

    # Cria o projeto com as informações fornecidas
    extra_context = {
        "connect_to_database": True,
        "database_type": database_type,
        "database_user": database_user,
        "database_password": database_password,
        "database_host": database_host,
        "database_name": database_name
    }
else:
    # Cria o projeto com valores padrão
    extra_context = {"connect_to_database": False}

# Usa o Cookiecutter para criar o projeto
cookiecutter(
    project_template,
    no_input=True,
    extra_context=extra_context
)

# Grava as informações do banco de dados no arquivo .env
if connect_to_database.lower() in ["yes", "y", "true"]:
    set_key('.env', 'DATABASE_TYPE', database_type)
    set_key('.env', 'DATABASE_USER', database_user)
    set_key('.env', 'DATABASE_PASSWORD', database_password)
    set_key('.env', 'DATABASE_HOST', database_host)
    set_key('.env', 'DATABASE_NAME', database_name)
else:
    set_key('.env', 'DATABASE_TYPE', 'none')
    set_key('.env', 'DATABASE_USER', 'none')
    set_key('.env', 'DATABASE_PASSWORD', 'none')
    set_key('.env', 'DATABASE_HOST', 'none')
    set_key('.env', 'DATABASE_NAME', 'none')

print("Arquivo .env criado com as informações do banco de dados.")
