import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    raise RuntimeError("Missing TOKEN environment variable. Get one from @BotFather.")
