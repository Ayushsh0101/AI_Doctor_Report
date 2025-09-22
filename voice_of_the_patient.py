# # # # # if you dont use pipenv uncomment the following:
# # # # # from dotenv import load_dotenv
# # # # # load_dotenv()

# # # # #Step1: Setup Audio recorder (ffmpeg & portaudio)
# # # # # ffmpeg, portaudio, pyaudio
# # # # import logging
# # # # import speech_recognition as sr
# # # # from pydub import AudioSegment
# # # # from io import BytesIO

# # # # logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # # # def record_audio(file_path, timeout=20, phrase_time_limit=None):
# # # #     """
# # # #     Simplified function to record audio from the microphone and save it as an MP3 file.

# # # #     Args:
# # # #     file_path (str): Path to save the recorded audio file.
# # # #     timeout (int): Maximum time to wait for a phrase to start (in seconds).
# # # #     phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
# # # #     """
# # # #     recognizer = sr.Recognizer()
    
# # # #     try:
# # # #         with sr.Microphone() as source:
# # # #             logging.info("Adjusting for ambient noise...")
# # # #             recognizer.adjust_for_ambient_noise(source, duration=1)
# # # #             logging.info("Start speaking now...")
            
# # # #             # Record the audio
# # # #             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
# # # #             logging.info("Recording complete.")
            
# # # #             # Convert the recorded audio to an MP3 file
# # # #             wav_data = audio_data.get_wav_data()
# # # #             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
# # # #             audio_segment.export(file_path, format="mp3", bitrate="128k")
            
# # # #             logging.info(f"Audio saved to {file_path}")

# # # #     except Exception as e:
# # # #         logging.error(f"An error occurred: {e}")

# # # # audio_filepath="patient_voice_test_for_patient.mp3"
# # # # #record_audio(file_path=audio_filepath)

# # # # #Step2: Setup Speech to text–STT–model for transcription
# # # # import os
# # # # from groq import Groq

# # # # GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
# # # # stt_model="whisper-large-v3"

# # # # def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
# # # #     client=Groq(api_key=GROQ_API_KEY)
    
# # # #     audio_file=open(audio_filepath, "rb")
# # # #     transcription=client.audio.transcriptions.create(
# # # #         model=stt_model,
# # # #         file=audio_file,
# # # #         language="en"
# # # #     )

# # # #     return transcription.text
# # # import logging
# # # import speech_recognition as sr
# # # from pydub import AudioSegment
# # # from io import BytesIO
# # # import os
# # # from dotenv import load_dotenv
# # # from groq import Groq

# # # # Logging setup
# # # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # # # Load environment variables
# # # load_dotenv()
# # # GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# # # if not GROQ_API_KEY:
# # #     raise RuntimeError("❌ GROQ_API_KEY not found in .env file")

# # # def record_audio(file_path, timeout=20, phrase_time_limit=None):
# # #     """Record audio from the microphone and save it as an MP3 file."""
# # #     recognizer = sr.Recognizer()

# # #     try:
# # #         with sr.Microphone() as source:
# # #             logging.info("Adjusting for ambient noise...")
# # #             recognizer.adjust_for_ambient_noise(source, duration=1)
# # #             logging.info("Start speaking now...")

# # #             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
# # #             logging.info("Recording complete.")

# # #             # Convert to MP3
# # #             wav_data = audio_data.get_wav_data()
# # #             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
# # #             audio_segment.export(file_path, format="mp3", bitrate="128k")

# # #             logging.info(f"Audio saved to {file_path}")

# # #     except Exception as e:
# # #         logging.error(f"An error occurred while recording: {e}")

# # # def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
# # #     """Transcribe audio using Groq Whisper model."""
# # #     client = Groq(api_key=GROQ_API_KEY)

# # #     with open(audio_filepath, "rb") as audio_file:
# # #         transcription = client.audio.transcriptions.create(
# # #             model=stt_model,
# # #             file=audio_file,
# # #             language="en"
# # #         )

# # #     return transcription.text
# # import logging
# # import speech_recognition as sr
# # from pydub import AudioSegment
# # from io import BytesIO
# # from groq import Groq
# # import os
# # from dotenv import load_dotenv

# # # ✅ Load API keys from .env
# # load_dotenv()
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # # ✅ Setup logging
# # logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # def record_audio(file_path, timeout=20, phrase_time_limit=None):
# #     """Record audio from the microphone and save it as an MP3 file."""
# #     recognizer = sr.Recognizer()

# #     try:
# #         with sr.Microphone() as source:
# #             logging.info("Adjusting for ambient noise...")
# #             recognizer.adjust_for_ambient_noise(source, duration=1)
# #             logging.info("Start speaking now...")

# #             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
# #             logging.info("Recording complete.")

# #             # Convert to MP3
# #             wav_data = audio_data.get_wav_data()
# #             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
# #             audio_segment.export(file_path, format="mp3", bitrate="128k")

# #             logging.info(f"Audio saved to {file_path}")

# #     except Exception as e:
# #         logging.error(f"An error occurred while recording: {e}")

# # def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
# #     """Transcribe audio using Groq Whisper model."""
# #     if not GROQ_API_KEY:
# #         raise ValueError("❌ GROQ_API_KEY is missing! Please check your .env file.")

# #     client = Groq(api_key=GROQ_API_KEY)

# #     with open(audio_filepath, "rb") as audio_file:
# #         transcription = client.audio.transcriptions.create(
# #             model=stt_model,
# #             file=audio_file,
# #             language="en"
# #         )

# #     return transcription.text
# # if __name__ == "__main__":
# #     # Test recording + transcription
# #     output_file = "patient_test.mp3"
# #     record_audio(output_file, timeout=10)  # record up to 10 seconds
    
# #     print("🎤 Recorded audio saved at:", output_file)

# #     if output_file:
# #         transcription = transcribe_with_groq(output_file)
# #         print("📝 Transcription:", transcription)
# import logging
# import speech_recognition as sr
# from pydub import AudioSegment
# from io import BytesIO
# from groq import Groq
# from config import GROQ_API_KEY  # ✅ centralized import

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# def record_audio(file_path, timeout=20, phrase_time_limit=None):
#     """Record audio from the microphone and save it as an MP3 file."""
#     recognizer = sr.Recognizer()

#     try:
#         with sr.Microphone() as source:
#             logging.info("Adjusting for ambient noise...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)
#             logging.info("Start speaking now...")

#             audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
#             logging.info("Recording complete.")

#             # Convert to MP3
#             wav_data = audio_data.get_wav_data()
#             audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
#             audio_segment.export(file_path, format="mp3", bitrate="128k")

#             logging.info(f"Audio saved to {file_path}")

#     except Exception as e:
#         logging.error(f"An error occurred while recording: {e}")

# def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
#     """Transcribe audio using Groq Whisper model."""
#     client = Groq(api_key=GROQ_API_KEY)

#     with open(audio_filepath, "rb") as audio_file:
#         transcription = client.audio.transcriptions.create(
#             model=stt_model,
#             file=audio_file,
#             language="en"
#         )

#     return transcription.text


# # ✅ Test block: runs only if you execute `python voice_of_the_patient.py`
# if __name__ == "__main__":
#     test_file = "patient_test.mp3"

#     # Step 1: Record audio
#     record_audio(test_file, timeout=10)
#     print(f"🎤 Recorded audio saved at: {test_file}")

#     # Step 2: Transcribe audio
#     try:
#         transcription = transcribe_with_groq(test_file)
#         print("📝 Transcription:", transcription)
#     except Exception as e:
#         print("❌ Error during transcription:", e)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq
from config import GROQ_API_KEY  # centralized import

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """Record audio from the microphone and save it as an MP3 file."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now...")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            # Convert recorded audio (wav) → MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while recording: {e}")


def transcribe_with_groq(audio_filepath, stt_model="whisper-large-v3"):
    """Transcribe audio using Groq Whisper model."""
    if not GROQ_API_KEY:
        raise RuntimeError("❌ GROQ_API_KEY not found. Please check your .env file.")

    client = Groq(api_key=GROQ_API_KEY)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text


# ✅ Run standalone for quick testing
if __name__ == "__main__":
    test_file = "patient_test.mp3"

    # Step 1: Record audio
    record_audio(test_file, timeout=10)
    print(f"🎤 Recorded audio saved at: {test_file}")

    # Step 2: Transcribe audio
    try:
        transcription = transcribe_with_groq(test_file)
        print("📝 Transcription:", transcription)
    except Exception as e:
        print("❌ Error during transcription:", e)
