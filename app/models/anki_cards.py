import re
from pathlib import Path
from dataclasses import dataclass
from typing import Protocol, ClassVar

from .domain import CardType


class AnkiCard(Protocol):
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]]

    @classmethod
    def create_from_csv(cls, row: dict) -> 'AnkiCard': ...

    def get_text_for_audio(self) -> str: ...

    def get_audio_filename(self) -> str: ...

    def to_anki_fields(self) -> list[str]: ...


@dataclass(slots=True)
class NumberCard:
    number: int
    word: str
    ipa: str
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {'number', 'word', 'ipa'}

    @classmethod
    def create_from_csv(cls, row: dict) -> 'NumberCard':
        return cls(
            number=int(row['number']),
            word=row['word'],
            ipa=row['ipa'],
        )

    def get_text_for_audio(self) -> str:
        return f'Numéro {self.number}'

    def get_audio_filename(self) -> str:
        return f"num_{self.word}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        return [
            str(self.number),
            self.word,
            self.ipa,
            audio_field
        ]


@dataclass(slots=True)
class VocabularyCard:
    spanish_words: str
    french_sentence: str
    ipa: str
    notes: str
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {'text_es', 'text_fr', 'ipa', 'notes'}

    @classmethod
    def create_from_csv(cls, row: dict) -> 'VocabularyCard':
        return cls(
            spanish_words=row['text_es'],
            french_sentence=row['text_fr'],
            ipa=row['ipa'],
            notes=row['notes'],
        )

    def get_text_for_audio(self) -> str:
        return self.french_sentence

    def get_audio_filename(self) -> str:
        safe_name = self.french_sentence[:30].replace(" ", "_").replace("'", "")
        return f"vocab_{safe_name}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        return [
            self.spanish_words,
            self.french_sentence,
            audio_field,
            self.notes
        ]


@dataclass(slots=True)
class ClozeCard:
    sentence: str
    translation: str
    notes: str
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {'text_cloze', 'translation', 'notes'}

    @classmethod
    def create_from_csv(cls, row: dict) -> 'ClozeCard':
        return cls(
            sentence=row['text_cloze'],
            translation=row['translation'],
            notes=row['notes'],
        )

    def get_clean_text(self) -> str:
        text_clean = re.sub(r'\{\{c\d+::(.*?)\}\}', r'\1', self.sentence)
        return text_clean

    def get_text_for_audio(self) -> str:
        return self.get_clean_text()

    def get_audio_filename(self) -> str:
        text = self.get_clean_text()
        clean = text[:30].replace(" ", "_").replace("'", "")
        return f"cloze_{clean}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        return [
            self.sentence,
            audio_field,
            self.translation,
            self.notes
        ]


def get_anki_card(card_type: CardType) -> AnkiCard:
    factories: dict[CardType, AnkiCard] = {
        CardType.NUMBER: NumberCard,
        CardType.CLOZE: ClozeCard,
        CardType.VOCABULARY: VocabularyCard
    }
    return factories[card_type]
