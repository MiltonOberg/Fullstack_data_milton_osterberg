from pathlib import Path

DATABASE_PATH = Path(__file__).parent/ "youtube_data.db"
CLEANED_DATA_PATH = Path(__file__).parent / "cleaned_data"
RAW_DATA_PATH = Path(__file__).parent/ "raw_data"
CSS_PATH= Path(__file__).parents[1]/ "frontend"/ "style.css"
BACKGOUND_IMAGE= Path(__file__).parents[1]/ "frontend"/ "dashboard_background.png"