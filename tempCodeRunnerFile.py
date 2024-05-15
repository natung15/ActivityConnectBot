from typing import Final
import os
import certifi
from dotenv import load_dotenv
from discord import Intents,Client, Message
from responses import get_response

os.environ["custom_cert_bundle.pem"] = certifi.where()
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

