import random
from pathlib import Path

import genanki

from models.anki_cards import AnkiCard
from models.registry import CardTypeConfig


class DeckBuilderService:

    @staticmethod
    def build(
            cards: list[AnkiCard], card_config: CardTypeConfig, deck_name: str,
            output_path: Path
    ):
        """Generates the .apkg file"""
        deck = genanki.Deck(
            deck_id=random.randrange(1 << 30, 1 << 31),
            name=deck_name
        )

        anki_model = card_config.anki_model
        for card in cards:
            note = genanki.Note(
                model=anki_model,
                fields=card.to_anki_fields()
            )
            deck.add_note(note)

        audio_files: list[Path] = [
            card.audio_path for card in cards if card.audio_path is not None
        ]
        image_files: list[Path] = [
            card.img_path for card in cards if card.img_path is not None
        ]
        package = genanki.Package(
            deck_or_decks=deck,
            media_files=audio_files + image_files
        )
        package.write_to_file(
            file=output_path
        )

        print(f"\n✅ Generated package: {output_path}")
        print(f"📦 Notes: {len(deck.notes)}")
        print(f'📦 Deck name: {deck_name}')
