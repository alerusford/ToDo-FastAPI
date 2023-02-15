from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name = 'ToDo FastAPI - Менеджер задач'
    db_url = 'sqlite:///.\\todo\\database\\DB\\todo.db'

settings = Settings()
