import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# Fail early if keys are missing
if not GROQ_API_KEY:
    raise RuntimeError("Missing GROQ_API_KEY in .env file")

if not ELEVEN_API_KEY:
    print("Warning: ELEVEN_API_KEY not found. ElevenLabs TTS will not work.")
