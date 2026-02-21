import sys
import logging
from pathlib import Path
from datetime import datetime


PACKAGE_DIR: Path = Path(__file__).parent.parent
LOGS_DIR = PACKAGE_DIR / 'logs'


def setup_logging(level: str = 'INFO'):
    """Configure logging for the application."""
    LOGS_DIR.mkdir(exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(module)-20s:%(lineno)-4d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(
                LOGS_DIR / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
            ),
            logging.StreamHandler(sys.stdout)
        ]
    )
