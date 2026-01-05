from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field, field_validator
from urllib.parse import urlparse
from typing import List, Union


class DatabaseSettings(BaseSettings):

    username: str = Field(alias="DB_POSTGRES_USER")
    password: str = Field(alias="DB_POSTGRES_PASSWORD")
    db_name: str = Field(alias="DB_POSTGRES_DB")
    host: str = Field(default="db", alias="DB_HOST")
    port: int = Field(default=5432, alias="DB_PORT")
    database_url: str = Field(alias="DATABASE_URL")
    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """A simple validator to ensure the URL looks like a postgres connection string."""
        if not v.startswith("postgresql://"):
            raise ValueError("DATABASE_URL must start with 'postgresql://'")
        return v

class Settings(BaseSettings):
    """
    Application settings, loaded from environment variables.
    """
    # --- Application Settings ---
    APP_TITLE: str = "Personal Library API"
    APP_VERSION: str = "1.0.0"
    
    # --- Server Settings ---
    HOST: str = "http://127.0.0.1"
    PORT: int = 8000
    
    # This tells Pydantic to load variables from a .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore" # Ignore any extra environment variables not defined in the model
        )

    # --- CORS Settings ---
    # Expect a comma-separated string of origins, e.g., "http://localhost:3000,https://example.com"
    BACKEND_CORS_ORIGINS: Union[List[str], str] = ["*"]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v):
        if isinstance(v, str) and not v.startswith("["):
            origins = [i.strip() for i in v.split(",")]
        elif isinstance(v, list):
            origins = v
        else:
            return v # Pass through to core validation to raise an error

        # New complex logic that only runs on lists
        for origin in origins:
            if not urlparse(origin).scheme:
                raise ValueError(f"Invalid origin URL: {origin}")
                
        return origins
    
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    SECRET_KEY: str

# Create a single settings instance to be used throughout the application
settings = Settings()