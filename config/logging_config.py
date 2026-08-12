import logging
from pathlib import Path


LOG_DIR = Path(__file__).resolve().parent.parent / "logs"


def configure_logging(component):
    LOG_DIR.mkdir(exist_ok=True)

    log_file = LOG_DIR / f"{component}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        encoding="utf-8",
        filename=log_file,
    )