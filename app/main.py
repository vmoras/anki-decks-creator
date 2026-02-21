import shutil
from pathlib import Path

import typer

from models.domain import CardType
from core.config import get_settings
from models.registry import CARD_REGISTRY
from services.loader_service import LoaderService
from services.builder_service import DeckBuilderService
from services.audio_generator_service import AudioService


app = typer.Typer(add_completion=False)


@app.command()
def main(
        card_type: CardType = typer.Argument(
            ..., help='Card type to create'
        ),
        input_file: Path = typer.Argument(
            ..., help='Path to the file to use to create the cards'
        ),
        deck_name: str = typer.Argument(
            ..., help='Name of the anki deck where the apkg will be assigned.'
        ),
        saving_dir: Path = typer.Option(
            Path(__file__).resolve().parent.parent / 'data' / 'output',
            help='Path to the directory where the apkg will be saved'
        ),
        output_name: str = typer.Option(
            None,
            help='Name for the output apkg file. If not provided, the card_type will be '
                 'used'
        ),
        create_audios: bool = typer.Option(
            True, help='Whether the app should create audios or not'
        ),
        save_audios: bool = typer.Option(
            True, help='Whether the audios generated should be kept or not'
        ),
        saved_audios_dir: Path = typer.Option(
            Path(__file__).resolve().parent.parent / 'data' / 'audios',
            help='Path where the audios are saved after being generated. Can be deleted '
                 'if save-audios is false'
        )
        
):
    # --------------------------------- Validations ---------------------------------
    if not input_file.exists():
        typer.echo(f'ERROR: input file {input_file} does not exists', err=True)
        raise typer.Exit(code=1)
    if input_file.suffix != '.csv':
        typer.echo(
            f'ERROR: input file {input_file} is not a propper CSV and the program '
            f'currently only supports CSV files.',
            err=True
        )
        raise typer.Exit(code=1)

    settings = get_settings()
    can_create_audio = settings.can_generate_audio
    if create_audios and not can_create_audio:
        typer.echo(
            f'ERROR: selected create audios but app can not create audios, probably an '
            f'API key is missing', err=True
        )
        raise typer.Exit(code=1)
    if not create_audios and save_audios:
        typer.echo(
            'WARNING: save_audios will be ignored since create_audios is set to False.',
            err=True
        )
        save_audios = False

    if not saving_dir.exists():
        typer.echo(
            f'INFO: saving dir {saving_dir} does not exists. It will be created.'
        )
        saving_dir.mkdir(parents=True)
    if output_name is None:
        output_name = card_type.value.lower()
        typer.echo(
            f'INFO: since output name is None, the card type will be used as output name:'
            f' {card_type.value.lower()}'
        )
    output_path = saving_dir / f'{output_name}.apkg'
    if output_path.exists():
        typer.confirm(
            f'WARNING: the apkg file {output_path} already exists. Do you want to '
            f'override it?', abort=True
        )

    # ------------------------------------ Print ------------------------------------
    typer.echo("\n" + "─" * 50)
    typer.echo("  Anki Deck Generator")
    typer.echo("─" * 50)
    typer.echo(f"  Card type     : {card_type.value}")
    typer.echo(f"  Input CSV     : {input_file}")
    typer.echo(f"  Deck name     : {deck_name}")
    typer.echo(f"  Output path   : {output_path}")
    typer.echo(f"  Create audios : {create_audios}")
    typer.echo(f"  Save audios   : {save_audios}")
    typer.echo("─" * 50 + "\n")

    # ------------------------------------ Run ------------------------------------
    _run(
        card_type=card_type, input_path=input_file, deck_name=deck_name,
        output_path=output_path, create_audios=create_audios, save_audios=save_audios,
        save_audios_dir=saved_audios_dir
    )


def _run(
        card_type: CardType, input_path: Path, deck_name: str, output_path: Path,
        create_audios: bool, save_audios: bool, save_audios_dir: Path
):
    settings = get_settings()
    card_config = CARD_REGISTRY[card_type]

    # ------------------------------- CARDS GENERATION -------------------------------
    print("📖 Read input file...")
    cards = LoaderService.load_data(
        input_file=input_path, card_config=card_config
    )

    # ------------------------------- AUDIO GENERATION -------------------------------
    generated_audios: list[Path] = []
    if create_audios:
        print("\n🎵 Generating audios...")
        audio_service = AudioService(
            api_key=settings.ELEVENLABS_API_KEY,
            voice_id=settings.VOICE_ID,
            model_id=settings.MODEL_ID,
            output_format=settings.OUTPUT_FORMAT,
            language_code=settings.LANGUAGE_CODE,
            saving_dir=save_audios_dir
        )
        generated_audios = audio_service.generate_audios(cards=cards)

    # ------------------------------- DECK GENERATION -------------------------------
    print("\n📦 Creating Anki package...")
    DeckBuilderService.build(
        cards=cards, card_config=card_config, deck_name=deck_name,
        output_path=output_path
    )

    # ---------------------------------- CLEANING -----------------------------------
    if create_audios and not save_audios and generated_audios:
        for audio_path in generated_audios:
            shutil.rmtree(audio_path)

    print("\n🎉 DONE!")


if __name__ == "__main__":
    app()
