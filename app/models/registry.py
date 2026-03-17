from dataclasses import dataclass

import genanki

from .domain import CardType
from .anki_models import get_anki_model
from .anki_cards import get_anki_card, AnkiCard


@dataclass(frozen=True)
class CardTypeConfig:
    anki_card: AnkiCard
    anki_model: genanki.Model


CARD_REGISTRY: dict[CardType, CardTypeConfig] = {
    CardType.NUMBER: CardTypeConfig(
        anki_card=get_anki_card(CardType.NUMBER),
        anki_model=get_anki_model(CardType.NUMBER)
    ),
    CardType.VOCABULARY: CardTypeConfig(
        anki_card=get_anki_card(CardType.VOCABULARY),
        anki_model=get_anki_model(CardType.VOCABULARY)
    ),
    CardType.CLOZE: CardTypeConfig(
        anki_card=get_anki_card(CardType.CLOZE),
        anki_model=get_anki_model(CardType.CLOZE)
    ),
    CardType.VERB: CardTypeConfig(
        anki_card=get_anki_card(CardType.VERB),
        anki_model=get_anki_model(CardType.VERB)
    )
}
