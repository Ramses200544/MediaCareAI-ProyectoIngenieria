from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "MediaCare AI"
    database_url: str = "/"
    model_config = SettingsConfigDict(file=".env")
settings = Settings()

print(settings.app_name)