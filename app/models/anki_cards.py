import re
from pathlib import Path
from dataclasses import dataclass
from typing import Protocol, ClassVar

from .domain import CardType


class AnkiCard(Protocol):
    create_img: bool = False
    img_path: Path | None = None
    img_prompt: str | None = None
    create_audio: bool = False
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]]  # Required columns in the CSV file

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
    create_img: bool = False
    img_path: Path | None = None
    img_prompt: str | None = None
    create_audio: bool = True
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
    french_word: str
    ipa: str
    notes: str
    create_img: bool
    img_path: Path | None
    img_prompt: str | None
    audio_script: str
    create_audio: bool = True
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {
        'word_spanish', 'word_french', 'audio_script', 'audio_ipa', 'notes', 'img_prompt',
        'img_name', 'create_img'
    }

    @classmethod
    def create_from_csv(cls, row: dict) -> 'VocabularyCard':
        """
        Note: for the image path, the image name is set now and its directory is later
        set.
        """
        if row['create_img'].lower() != 'true':
            img_prompt, img_path = None, None
            create_img = False
        else:
            img_prompt, img_path = row['img_prompt'], Path(f"{row['img_name']}")
            create_img = True

        return cls(
            spanish_words=row['word_spanish'],
            french_word=row['word_french'],
            ipa=row['audio_ipa'],
            notes=row['notes'],
            audio_script=row['audio_script'],
            img_path=img_path,
            img_prompt=img_prompt,
            create_img=create_img
        )

    def get_text_for_audio(self) -> str:
        return self.audio_script

    def get_audio_filename(self) -> str:
        safe_name = re.sub(r'[^\w\-.]', '_', self.french_word)
        return f"vocab_{safe_name}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        img_field = f'<img src="{self.img_path.name}">' if self.img_path is not None else ""
        return [
            self.spanish_words,
            self.french_word,
            audio_field,
            self.ipa,
            img_field,
            self.notes
        ]


@dataclass(slots=True)
class ClozeCard:
    sentence: str
    translation: str
    notes: str
    create_img: bool = False
    img_path: Path | None = None
    img_prompt: str | None = None
    create_audio: bool = True
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
        text_clean = re.sub(r'\{\{c\d+::(.*?)}}', r'\1', self.sentence)
        return text_clean

    def get_text_for_audio(self) -> str:
        return self.get_clean_text()

    def get_audio_filename(self) -> str:
        clean = re.sub(r'[^\w\-.]', '_', self.sentence)
        return f"cloze_{clean}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        return [
            self.sentence,
            audio_field,
            self.translation,
            self.notes
        ]


@dataclass(slots=True)
class VerbCard:
    verb_spanish: str
    conjugation: str
    notes: str
    audio_script: str
    create_img: bool = False
    img_path: Path | None = None
    img_prompt: str | None = None
    create_audio: bool = True
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {
        'verb_spanish', 'conjugation', 'notes', 'audio_script'
    }

    @classmethod
    def create_from_csv(cls, row: dict) -> 'VerbCard':
        return cls(
            verb_spanish=row['verb_spanish'],
            conjugation=row['conjugation'],
            notes=row['notes'],
            audio_script=row['audio_script']
        )

    def get_text_for_audio(self) -> str:
        return self.audio_script

    def get_audio_filename(self) -> str:
        clean = re.sub(r'[^\w\-.]', '_', self.verb_spanish)
        return f"verb_{clean}.mp3"

    def to_anki_fields(self) -> list[str]:
        audio_field = f"[sound:{self.get_audio_filename()}]" if self.audio_path else ""
        return [
            self.verb_spanish,
            self.conjugation,
            self.notes,
            audio_field
        ]


@dataclass(slots=True)
class GrammarCard:
    topic: str
    description: str
    instruction: str
    create_img: bool = False
    img_path: Path | None = None
    img_prompt: str | None = None
    create_audio: bool = False
    audio_path: Path | None = None
    REQUIRED_FIELDS: ClassVar[set[str]] = {
        'topic', 'instruction'
    }

    @classmethod
    def create_from_csv(cls, row: dict) -> 'GrammarCard':
        return cls(
            topic=row['topic'],
            description=row['description'],
            instruction=row['instruction']
        )

    def get_text_for_audio(self) -> str:
        raise NotImplementedError("GrammarCard does not support audio")

    def get_audio_filename(self) -> str:
        raise NotImplementedError("GrammarCard does not support audio")

    def to_anki_fields(self) -> list[str]:
        return [
            self.topic,
            self.description,
            self.instruction
        ]



def get_anki_card(card_type: CardType) -> AnkiCard:
    factories: dict[CardType, AnkiCard] = {
        CardType.NUMBER: NumberCard,
        CardType.CLOZE: ClozeCard,
        CardType.VOCABULARY: VocabularyCard,
        CardType.VERB: VerbCard,
        CardType.GRAMMAR: GrammarCard
    }
    return factories[card_type]
