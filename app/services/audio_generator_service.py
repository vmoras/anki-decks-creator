import logging
from pathlib import Path

from tqdm import tqdm
from elevenlabs import ElevenLabs

from models.anki_cards import AnkiCard


logger = logging.getLogger(__name__)


class AudioService:

    def __init__(
            self,
            voice_id: str,
            model_id: str,
            output_format: str,
            language_code: str,
            api_key: str,
            saving_dir: Path
    ):
        self.voice_id: str = voice_id
        self.model_id: str = model_id
        self.output_format: str = output_format
        self.language_code: str = language_code
        self.elevenlabs: ElevenLabs = ElevenLabs(api_key=api_key)
        self.saving_dir: Path = saving_dir

        self.saving_dir.mkdir(parents=True, exist_ok=True)

        logger.info(
            f'AudioService initialized with voice_id={voice_id}, '
            f'model_id={model_id}, output_format={output_format}, '
            f'language_code={language_code}'
        )

    def generate_audios(self, cards: list[AnkiCard]) -> list[Path]:
        generated_audios: list[Path] = []
        for card in tqdm(cards):
            audio_path = self._get_audio(card)
            card.audio_path = audio_path
            generated_audios.append(audio_path)
        return generated_audios

    def _get_audio(self, card: AnkiCard) -> Path:
        try:
            text = card.get_text_for_audio()
            filename = card.get_audio_filename()

            # Check if audio exists
            output_file = self.saving_dir / filename
            if output_file.exists():
                logger.info(f'Omitting audio creation, file already exists')
                return output_file

            # Get audio from ElevenLabs
            logger.info(f'Getting audio from text: {text}')
            audio = self.elevenlabs.text_to_speech.convert(
                text=text,
                voice_id=self.voice_id,
                model_id=self.model_id,
                output_format=self.output_format,
                language_code=self.language_code
            )

            # Save audio to file
            logger.info('Saving audio to file')
            with open(output_file, 'wb') as f:
                for chunk in audio:
                    f.write(chunk)

            logger.info(f'Audio saved to file: {output_file}')
            return output_file

        except Exception:
            logger.exception('Error generating audio')
            raise
