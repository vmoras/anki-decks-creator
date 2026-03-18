import time
import logging
import requests
import traceback
from pathlib import Path

from tqdm import tqdm

from models.anki_cards import AnkiCard

logger = logging.getLogger(__name__)


class ImageService:

    def __init__(
            self,
            token: str,
            saving_dir: Path
    ):
        self.token: str = token
        self.saving_dir: Path = saving_dir
        self.api_url: str = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

        self.saving_dir.mkdir(parents=True, exist_ok=True)

        logger.info(
            f'ImageService initialized with saving_dir={self.saving_dir}'
        )

    def get_images(self, cards: list[AnkiCard]) -> list[Path]:
        downloaded_images: list[Path] = list()

        for card in tqdm(cards):
            if not card.create_img:
                continue

            filename = card.img_path.with_suffix('.png')
            output_path = self.saving_dir / filename
            if not output_path.exists():
                self._generate_image(card.img_prompt, output_path)

            card.img_path = output_path
            downloaded_images.append(output_path)
            time.sleep(1)

        return downloaded_images

    def _generate_image(self, prompt: str, output_path: Path) -> None:
        try:
            response = requests.post(
                self.api_url,
                headers={"Authorization": f"Bearer {self.token}"},
                json={
                    "inputs": prompt,
                    "parameters": {
                        "width": 512,
                        "height": 512
                    }
                }
            )
            if response.status_code == 200:
                output_path.write_bytes(response.content)
                return
            else:
                print(response.status_code)
                return
        except:
            traceback.print_exc()
            return
