# # # # # if you dont use pipenv uncomment the following:
# # # # # from dotenv import load_dotenv
# # # # # load_dotenv()

# # # # #Step1a: Setup Text to Speech–TTS–model with gTTS
# # # # import os
# # # # from gtts import gTTS

# # # # def text_to_speech_with_gtts_old(input_text, output_filepath):
# # # #     language="en"

# # # #     audioobj= gTTS(
# # # #         text=input_text,
# # # #         lang=language,
# # # #         slow=False
# # # #     )
# # # #     audioobj.save(output_filepath)


# # # # input_text="Hi this is Ai with Hassan!"
# # # # text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# # # # #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# # # # import elevenlabs
# # # # from elevenlabs.client import ElevenLabs

# # # # ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

# # # # def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
# # # #     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
# # # #     audio=client.generate(
# # # #         text= input_text,
# # # #         voice= "Aria",
# # # #         output_format= "mp3_22050_32",
# # # #         model= "eleven_turbo_v2"
# # # #     )
# # # #     elevenlabs.save(audio, output_filepath)

# # # # #text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# # # # #Step2: Use Model for Text output to Voice

# # # # import subprocess
# # # # import platform

# # # # def text_to_speech_with_gtts(input_text, output_filepath):
# # # #     language="en"

# # # #     audioobj= gTTS(
# # # #         text=input_text,
# # # #         lang=language,
# # # #         slow=False
# # # #     )
# # # #     audioobj.save(output_filepath)
# # # #     os_name = platform.system()
# # # #     try:
# # # #         if os_name == "Darwin":  # macOS
# # # #             subprocess.run(['afplay', output_filepath])
# # # #         elif os_name == "Windows":  # Windows
# # # #             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# # # #         elif os_name == "Linux":  # Linux
# # # #             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
# # # #         else:
# # # #             raise OSError("Unsupported operating system")
# # # #     except Exception as e:
# # # #         print(f"An error occurred while trying to play the audio: {e}")


# # # # input_text="Hi this is Ai with Hassan, autoplay testing!"
# # # # #text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")


# # # # def text_to_speech_with_elevenlabs(input_text, output_filepath):
# # # #     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
# # # #     audio=client.generate(
# # # #         text= input_text,
# # # #         voice= "Aria",
# # # #         output_format= "mp3_22050_32",
# # # #         model= "eleven_turbo_v2"
# # # #     )
# # # #     elevenlabs.save(audio, output_filepath)
# # # #     os_name = platform.system()
# # # #     try:
# # # #         if os_name == "Darwin":  # macOS
# # # #             subprocess.run(['afplay', output_filepath])
# # # #         elif os_name == "Windows":  # Windows
# # # #             subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# # # #         elif os_name == "Linux":  # Linux
# # # #             subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
# # # #         else:
# # # #             raise OSError("Unsupported operating system")
# # # #     except Exception as e:
# # # #         print(f"An error occurred while trying to play the audio: {e}")

# # # # #text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3") 
# # # import os
# # # import platform
# # # import subprocess
# # # from gtts import gTTS
# # # import elevenlabs
# # # from elevenlabs.client import ElevenLabs
# # # from dotenv import load_dotenv

# # # # Load environment variables
# # # load_dotenv()
# # # ELEVENLABS_API_KEY = os.getenv("ELEVEN_API_KEY")

# # # # -------------------------
# # # # Google TTS (gTTS)
# # # # -------------------------
# # # def text_to_speech_with_gtts(input_text, output_filepath):
# # #     """Convert text to speech with gTTS and play automatically."""
# # #     language = "en"

# # #     audioobj = gTTS(text=input_text, lang=language, slow=False)
# # #     audioobj.save(output_filepath)

# # #     os_name = platform.system()
# # #     try:
# # #         if os_name == "Darwin":  # macOS
# # #             subprocess.run(["afplay", output_filepath])
# # #         elif os_name == "Windows":  # Windows
# # #             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# # #         elif os_name == "Linux":  # Linux
# # #             subprocess.run(["aplay", output_filepath])  # alternative: mpg123 / ffplay
# # #         else:
# # #             raise OSError("Unsupported operating system")
# # #     except Exception as e:
# # #         print(f"An error occurred while trying to play the audio: {e}")

# # #     return output_filepath


# # # # -------------------------
# # # # ElevenLabs TTS
# # # # -------------------------
# # # def text_to_speech_with_elevenlabs(input_text, output_filepath):
# # #     """Convert text to speech with ElevenLabs (requires ELEVEN_API_KEY)."""
# # #     if not ELEVENLABS_API_KEY:
# # #         raise RuntimeError("❌ ELEVEN_API_KEY not found in .env file")

# # #     client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
# # #     audio = client.generate(
# # #         text=input_text,
# # #         voice="Aria",
# # #         output_format="mp3_22050_32",
# # #         model="eleven_turbo_v2"
# # #     )
# # #     elevenlabs.save(audio, output_filepath)

# # #     os_name = platform.system()
# # #     try:
# # #         if os_name == "Darwin":
# # #             subprocess.run(["afplay", output_filepath])
# # #         elif os_name == "Windows":
# # #             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# # #         elif os_name == "Linux":
# # #             subprocess.run(["aplay", output_filepath])
# # #         else:
# # #             raise OSError("Unsupported operating system")
# # #     except Exception as e:
# # #         print(f"An error occurred while trying to play the audio: {e}")

# # #     return output_filepath
# # import os
# # import platform
# # import subprocess
# # from gtts import gTTS
# # import elevenlabs
# # from elevenlabs.client import ElevenLabs
# # from config import ELEVEN_API_KEY  # ✅ centralized import

# # # -------------------------
# # # Google TTS (gTTS)
# # # -------------------------
# # def text_to_speech_with_gtts(input_text, output_filepath):
# #     """Convert text to speech with gTTS and play automatically."""
# #     language = "en"

# #     audioobj = gTTS(text=input_text, lang=language, slow=False)
# #     audioobj.save(output_filepath)

# #     os_name = platform.system()
# #     try:
# #         if os_name == "Darwin":  # macOS
# #             subprocess.run(["afplay", output_filepath])
# #         elif os_name == "Windows":  # Windows
# #             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# #         elif os_name == "Linux":  # Linux
# #             subprocess.run(["aplay", output_filepath])  # alternative: mpg123 / ffplay
# #         else:
# #             raise OSError("Unsupported operating system")
# #     except Exception as e:
# #         print(f"An error occurred while trying to play the audio: {e}")

# #     return output_filepath

# # # -------------------------
# # # ElevenLabs TTS
# # # -------------------------
# # def text_to_speech_with_elevenlabs(input_text, output_filepath):
# #     """Convert text to speech with ElevenLabs (requires ELEVEN_API_KEY)."""
# #     if not ELEVEN_API_KEY:
# #         raise RuntimeError("❌ ELEVEN_API_KEY not found in .env file")

# #     client = ElevenLabs(api_key=ELEVEN_API_KEY)
# #     audio = client.generate(
# #         text=input_text,
# #         voice="Aria",
# #         output_format="mp3_22050_32",
# #         model="eleven_turbo_v2"
# #     )
# #     elevenlabs.save(audio, output_filepath)

# #     os_name = platform.system()
# #     try:
# #         if os_name == "Darwin":
# #             subprocess.run(["afplay", output_filepath])
# #         elif os_name == "Windows":
# #             subprocess.run(["powershell", "-c", f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
# #         elif os_name == "Linux":
# #             subprocess.run(["aplay", output_filepath])
# #         else:
# #             raise OSError("Unsupported operating system")
# #     except Exception as e:
# #         print(f"An error occurred while trying to play the audio: {e}")

# #     return output_filepath
# # import logging
# # import os
# # from dotenv import load_dotenv
# # from elevenlabs import ElevenLabs

# # # ✅ Load API keys from .env
# # load_dotenv()
# # ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# # # ✅ Setup logging
# # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # def text_to_speech_with_elevenlabs(input_text, output_filepath="doctor_voice.mp3", voice="Rachel"):
# #     """Convert text to speech using ElevenLabs API and save as MP3."""
# #     if not ELEVEN_API_KEY:
# #         raise ValueError("❌ ELEVEN_API_KEY is missing! Please check your .env file.")

# #     try:
# #         client = ElevenLabs(api_key=ELEVEN_API_KEY)

# #         logging.info("Sending text to ElevenLabs for TTS...")

# #         audio = client.generate(
# #             text=input_text,
# #             voice=voice,
# #             model="eleven_multilingual_v2"
# #         )

# #         with open(output_filepath, "wb") as f:
# #             f.write(audio)

# #         logging.info(f"✅ Doctor's voice saved to {output_filepath}")
# #         return output_filepath

# #     except Exception as e:
# #         logging.error(f"❌ Error generating speech with ElevenLabs: {e}")
# #         return None
# import logging
# import os
# from dotenv import load_dotenv
# from elevenlabs import ElevenLabs

# # Load API key
# load_dotenv()
# ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# def text_to_speech_with_elevenlabs(input_text, output_filepath="doctor_voice.mp3", voice="Rachel"):
#     """Convert text to speech using ElevenLabs API and save as MP3."""
#     if not ELEVEN_API_KEY:
#         raise ValueError("❌ ELEVEN_API_KEY is missing! Please check your .env file.")

#     try:
#         client = ElevenLabs(api_key=ELEVEN_API_KEY)

#         logging.info("Sending text to ElevenLabs for TTS...")

#         with client.text_to_speech.convert(
#             voice_id=voice,
#             model_id="eleven_multilingual_v2",
#             text=input_text
#         ) as audio_stream:
#             with open(output_filepath, "wb") as f:
#                 for chunk in audio_stream:
#                     f.write(chunk)

#         logging.info(f"✅ Doctor's voice saved to {output_filepath}")
#         return output_filepath

#     except Exception as e:
#         logging.error(f"❌ Error generating speech with ElevenLabs: {e}")
#         return None   
# if __name__ == "__main__":
#     test_text = "Hello, I am your AI doctor. I will take care of you."
#     output_file = text_to_speech_with_elevenlabs(test_text, output_filepath="doctor_voice.mp3")

#     if output_file and os.path.exists(output_file):
#         print(f"✅ Test successful! File saved: {output_file}")
#     else:
#         print("❌ Test failed. No audio file generated.")

import logging
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

# ✅ Load API keys from .env
load_dotenv()
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

# ✅ Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def text_to_speech_with_elevenlabs(input_text, output_filepath="doctor_voice.mp3", voice_id="21m00Tcm4TlvDq8ikWAM"):
    if not ELEVEN_API_KEY:
        raise ValueError("❌ ELEVEN_API_KEY is missing! Please check your .env file.")

    try:
        from elevenlabs.client import ElevenLabs
        client = ElevenLabs(api_key=ELEVEN_API_KEY)

        logging.info("Sending text to ElevenLabs for TTS...")

        audio = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            text=input_text
        )

        with open(output_filepath, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        logging.info(f"✅ Doctor's voice saved to {output_filepath}")
        return output_filepath

    except Exception as e:
        logging.error(f"❌ Error generating speech with ElevenLabs: {e}")
        return None


# ✅ Test block
if __name__ == "__main__":
    test_text = "Hello, I am your AI doctor. I will take care of you."
    output_file = text_to_speech_with_elevenlabs(test_text, output_filepath="doctor_voice.mp3")

    if output_file and os.path.exists(output_file):
        print(f"✅ Test successful! File saved: {output_file}")
    else:
        print("❌ Test failed. No audio file generated.")

