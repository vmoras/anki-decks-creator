from pathlib import Path
from functools import lru_cache

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_DIR: Path = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_DIR / '.env',
        env_file_encoding='utf-8'
    )

    ELEVENLABS_API_KEY : str | None = Field(None)
    VOICE_ID: str | None = Field(None)
    MODEL_ID: str | None = Field(None)
    OUTPUT_FORMAT: str | None = Field(None)
    LANGUAGE_CODE: str | None = Field(None)

    @model_validator(mode='after')
    def validate_audio_config(self) -> 'Settings':
        audio_fields: dict[str, str | None] = {
            'ELEVENLABS_API_KEY': self.ELEVENLABS_API_KEY,
            'VOICE_ID': self.VOICE_ID,
            'MODEL_ID': self.MODEL_ID,
            'OUTPUT_FORMAT': self.OUTPUT_FORMAT,
            'LANGUAGE_CODE': self.LANGUAGE_CODE,
        }
        missing = [k for k, v in audio_fields.items() if v is None]
        present = [k for k, v in audio_fields.items() if v is not None]

        if missing and present:
            raise ValueError(f"Partial audio config: missing {missing}")
        return self

    @property
    def can_generate_audio(self) -> bool:
        return self.ELEVENLABS_API_KEY is not None


@lru_cache
def get_settings() -> Settings:
    return Settings()