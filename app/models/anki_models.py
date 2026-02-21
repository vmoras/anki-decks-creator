from typing import Callable

import genanki

from .domain import CardType


MODEL_IDS: dict[CardType, float] = {
    CardType.NUMBER: 1607392321,
    CardType.VOCABULARY: 1607392322,
    CardType.CLOZE: 1607392323,
}


def _create_number_model() -> genanki.Model:
    return genanki.Model(
        MODEL_IDS[CardType.NUMBER],
        'Nombres',
        fields = [
            {'name': 'Number'},
            {'name': 'Word'},
            {'name': 'IPA'},
            {'name': 'Audio'},
        ],
        templates = [
            # TEMPLATE 1: Número → Audio + IPA + Word
            {
                'name': 'Number → Pronunciation',
                'qfmt': '''
                    <div style="font-size: 80px; text-align: center; color: #333;">
                        {{Number}}
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr>
                    <div style="font-size: 30px; text-align: center; margin-top: 20px;">
                        {{Audio}}
                    </div>
                    <div style="font-size: 40px; text-align: center; color: #666; margin-top: 15px;">
                        {{IPA}}
                    </div>
                    <div style="font-size: 50px; text-align: center; color: #2196F3; margin-top: 15px;">
                        {{Word}}
                    </div>
                '''
            },
            # TEMPLATE 2: Audio + IPA → Numero + Word
            {
                'name': 'Pronunciation → Numero',
                'qfmt': '''
                    <div style="font-size: 30px; text-align: center; margin-bottom: 20px;">
                        {{Audio}}
                    </div>
                    <div style="font-size: 40px; text-align: center; color: #666; margin-top: 20px;">
                        {{IPA}}
                    </div>
                    <div style="font-size: 20px; text-align: center; color: #999; margin-top: 30px;">
                        ¿Qué número es?
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr>
                    <div style="font-size: 80px; text-align: center; margin-top: 20px; color: #333;">
                        {{Number}}
                    </div>
                    <div style="font-size: 50px; text-align: center; color: #2196F3; margin-top: 15px;">
                        {{Word}}
                    </div>
                ''',
            }
        ]
    )


def _create_vocabulary_model() -> genanki.Model:
    return genanki.Model(
        MODEL_IDS[CardType.VOCABULARY],
        'Vocabulaire',
        fields=[
            {'name': 'Text_ES'},
            {'name': 'Text_FR'},
            {'name': 'Audio'},
            {'name': 'Notes'},
        ],
        templates=[
            # ES → FR
            {
                'name': 'ES → FR',
                'qfmt': '''
                    <div style="font-size: 40px; text-align: center;">
                        {{Text_ES}}
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr>
                    <div style="font-size: 30px; text-align: center; margin-top: 20px;">
                        {{Audio}}
                    </div>
                    <div style="font-size: 40px; text-align: center; color: #2196F3; margin-top: 15px;">
                        {{Text_FR}}
                    </div>
                    <div style="font-size: 25px; text-align: center; color: #666; margin-top: 15px;">
                        {{Notes}}
                    </div>
                '''
            },
            # FR → ES
            {
                'name': 'FR → ES',
                'qfmt': '''
                    <div style="font-size: 30px; text-align: center; margin-bottom: 20px;">
                        {{Audio}}
                    </div>
                    <div style="font-size: 40px; text-align: center; color: #2196F3;">
                        {{Text_FR}}
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr>
                    <div style="font-size: 40px; text-align: center; margin-top: 20px;">
                        {{Text_ES}}
                    </div>
                    <div style="font-size: 25px; text-align: center; color: #666; margin-top: 15px;">
                        {{Notes}}
                    </div>
                '''
            }
        ],
    )


def _create_cloze_model() -> genanki.Model:
    return genanki.Model(
        MODEL_IDS[CardType.CLOZE],
        'Cloze',
        model_type=genanki.Model.CLOZE,
        fields=[
            {'name': 'Text'},
            {'name': 'Audio'},
            {'name': 'Translation'},
            {'name': 'Notes'},
        ],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '''
                    <div style="font-size: 30px; text-align: center; margin-bottom: 20px;">
                        {{Audio}}
                    </div>
                    <div style="font-size: 40px; text-align: center;">
                        {{cloze:Text}}
                    </div>
                    <div style="font-size: 25px; text-align: center; color: #666; margin-top: 20px;">
                        {{Translation}}
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr>
                    <div style="font-size: 25px; text-align: center; color: #999; margin-top: 20px;">
                        {{Notes}}
                    </div>
                '''
            }
        ],
    )


def get_anki_model(card_type: CardType) -> genanki.Model:
    factories: dict[CardType, Callable[[], genanki.Model]] = {
        CardType.NUMBER: _create_number_model,
        CardType.VOCABULARY: _create_vocabulary_model,
        CardType.CLOZE: _create_cloze_model,
    }
    return factories[card_type]()
