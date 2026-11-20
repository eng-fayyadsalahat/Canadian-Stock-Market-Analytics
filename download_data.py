import gdown
from pathlib import Path
import logging


# --------------------------------
# Configuration
# --------------------------------

DATA_DIR = Path("data/processed")
DATA_DIR.mkdir(parents=True, exist_ok=True)

FILES = {
    "daily_data.csv": "1_o7URlWhXEt84q1cmLG3C-1kOml2ZUIU",
    "stock_predictions.csv": "1XwYXy0dPIBtMBxBxlk8YGqrIHyDENtbR",
    "market_data.csv": "1dzm-lzDy7ReAMGoH2dmXU6J6EE3aMPvw"
}

# https://drive.google.com/file/d/1_o7URlWhXEt84q1cmLG3C-1kOml2ZUIU
# https://drive.google.com/file/d/1dzm-lzDy7ReAMGoH2dmXU6J6EE3aMPvw/
# https://drive.google.com/file/d/1XwYXy0dPIBtMBxBxlk8YGqrIHyDENtbR/

# --------------------------------
# Download Files
# --------------------------------

def download_files():

    for filename, file_id in FILES.items():

        output_path = DATA_DIR / filename

        if output_path.exists():
            output_path.unlink()

        url = f"https://drive.google.com/uc?id={file_id}"

        print(f"Downloading {filename}...")

        result = gdown.download(
            url=url,
            output=str(output_path),
            quiet=False,
            fuzzy=True
        )

        if result is None:
            raise RuntimeError(
                f"Failed to download {filename}"
            )

        if not output_path.exists() or output_path.stat().st_size == 0:
            raise RuntimeError(
                f"Downloaded file is missing or empty: {filename}"
            )

        print(f"Downloaded successfully: {filename}")


if __name__ == "__main__":
    download_files()


