# .env ファイルをロードして環境変数へ反映
from dotenv import load_dotenv
load_dotenv()
import os

project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
processor_id = os.getenv("PROCESSOR_ID")
file_path = os.getenv('FILE_PATH')