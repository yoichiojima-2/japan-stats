import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
DATA_PATH = Path(os.getenv("APPROOT")) / "data"