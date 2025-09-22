import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

# Load API key
load_dotenv()
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

if not ELEVEN_API_KEY:
    raise ValueError("❌ ELEVEN_API_KEY missing. Check your .env file.")

client = ElevenLabs(api_key=ELEVEN_API_KEY)

# Fetch available voices
voices = client.voices.get_all()

print("🎤 Available Voices:")
for v in voices.voices:
    print(f"- {v.name} ({v.voice_id})")
