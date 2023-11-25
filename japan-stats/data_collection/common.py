import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
DATA_PATH = Path(os.getenv("APPROOT")) / "data"
