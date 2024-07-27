"""Environment configuration for Factool. """
import pydantic
from pydantic_settings import BaseSettings

class FactoolEnvConfig(BaseSettings, frozen=True):
    """Environment configuration for Factool."""

    openai_api_key: str = pydantic.Field(
        default="",
        env="OPENAI_API_KEY",
        description="API key for OpenAI",
    )

    serper_api_key: str = pydantic.Field(
        default="",
        env="SERPER_API_KEY",
        description="Key for Serper",
    )

    scraper_api_key: str = pydantic.Field(
        default="",
        env="SCRAPER_API_KEY",
        description="Key for Scraper",
    )

factool_env_config = FactoolEnvConfig()
