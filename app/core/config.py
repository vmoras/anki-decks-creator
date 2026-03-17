from pathlib import Path
from functools import lru_cache

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_DIR: Path = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / '.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )

    elevenlabs_api_key : str | None = Field(None)
    voice_id: str | None = Field(None)
    model_id: str | None = Field(None)
    output_format: str | None = Field(None)
    language_code: str | None = Field(None)
    
    pexels_api_key: str | None = Field(None)

    @model_validator(mode='after')
    def validate_audio_config(self) -> 'Settings':
        audio_fields: dict[str, str | None] = {
            'elevenlabs_api_key': self.elevenlabs_api_key,
            'voice_id': self.voice_id,
            'model_id': self.model_id,
            'output_format': self.output_format,
            'language_code': self.language_code,
        }
        missing = [k for k, v in audio_fields.items() if v is None]
        present = [k for k, v in audio_fields.items() if v is not None]

        if missing and present:
            raise ValueError(f"Partial audio config: missing {missing}")
        return self

    @property
    def can_generate_audio(self) -> bool:
        return self.elevenlabs_api_key is not None

    @property
    def can_get_images(self) -> bool:
        return self.pexels_api_key is not None


@lru_cache
def get_settings() -> Settings:
    return Settings()
