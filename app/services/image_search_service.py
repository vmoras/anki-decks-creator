import logging
import requests
from PIL import Image
import urllib.request
from io import BytesIO
from pathlib import Path

from tqdm import tqdm

from models.anki_cards import AnkiCard

logger = logging.getLogger(__name__)


class ImageService:

    def __init__(
            self,
            api_key: str,
            saving_dir: Path
    ):
        self.api_key: str = api_key
        self.saving_dir = saving_dir

        self.saving_dir.mkdir(parents=True, exist_ok=True)

        logger.info(
            f'ImageService initialized with saving_dir={self.saving_dir}'
        )

    def get_images(self, cards: list[AnkiCard]) -> list[Path]:
        downloaded_images: list[Path] = list()

        for card in tqdm(cards):
            if card.img_name is None:
                continue
            if not card.create_img:
                continue

            img_url = self._get_url(card.img_name)
            if img_url is None:
                continue

            output_path = self.saving_dir / f'{card.img_name}.png'
            if not output_path.exists():
                self._download_image(img_url, output_path)

            card.img_path = output_path
            downloaded_images.append(output_path)

        return downloaded_images

    def _get_url(self, img_name: str) -> str | None:
        headers = {"Authorization": self.api_key}
        params = {
            "query": img_name,
            "per_page": 1
        }

        try:
            res = requests.get(
                "https://api.pexels.com/v1/search", headers=headers,
                params=params
            )

            if res.status_code != 200:
                return None

            data = res.json()
            if not data["photos"]:
                return None

            image_url = data["photos"][0]["src"]["medium"]
            return image_url

        except Exception as e:
            print(f"❌ Pexels error: {e}")
            return None

    def _download_image(self, img_url: str, output_path: Path) -> None:
        print(img_url)
        req = urllib.request.Request(img_url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req).read()
        img = Image.open(BytesIO(data))
        img.save(output_path, "PNG")

        return
