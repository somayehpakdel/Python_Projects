from pydantic_settings import BaseSettings
from pydantic import Field

class FrontendSettings(BaseSettings):
    """
    Frontend-specific settings, loaded from environment variables.
    """
    # The URL of the backend API.
    # When running locally outside Docker, this defaults to the host machine.
    # When running in Docker, this will be overridden by docker-compose.yml.
    API_URL: str = Field(
        default="http://127.0.0.1:8000",
        description="The URL of the backend API service."
    )

# Create a single settings instance to be used throughout the frontend app
settings = FrontendSettings()