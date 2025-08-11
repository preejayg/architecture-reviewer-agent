from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    
    TOGETHER_API_KEY: str
    MODEL_NAME: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"

settings = Settings()
