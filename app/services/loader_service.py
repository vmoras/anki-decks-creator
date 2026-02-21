import csv

from pathlib import Path

from models.anki_cards import AnkiCard
from models.registry import CardTypeConfig


class LoaderService:

    @staticmethod
    def load_data(
            input_file: Path, card_config: CardTypeConfig
    ) -> list[AnkiCard]:
        if input_file.suffix == '.csv':
            return LoaderService._read_csv(
                filepath=input_file, anki_card=card_config.anki_card
            )
        raise ValueError(
            f'Input file {input_file} has non supported extension: {input_file.suffix}'
        )


    @staticmethod
    def _read_csv(filepath: Path, anki_card: AnkiCard) -> list[AnkiCard]:
        cards = []

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                # Make sure the CSV contains the correct column names
                column_names = reader.fieldnames
                missing = anki_card.REQUIRED_FIELDS - {c for c in column_names}
                if missing:
                    raise ValueError(
                        f"Missing required columns {sorted(missing)} in row with keys: "
                        f"{sorted(column_names)}"
                    )

                # Create each card based on each row from the CSV
                for row in reader:
                    card = anki_card.create_from_csv(row)
                    cards.append(card)
            return cards

        except:
            raise
