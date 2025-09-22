**AI Doctor – Voice & Vision Assistant**
An AI-powered healthcare assistant that allows patients to interact with doctors using voice and image inputs.
It integrates speech recognition, image analysis, and an advanced language model to provide medical insights. The system also replies in a doctor’s voice for a natural conversation flow.

**Features**
1 User Authentication – Secure login & registration with hashed passwords
2 Speech-to-Text – Converts patient queries into text
3 Image Analysis – Upload medical images (X-rays, skin images, etc.) for AI-based insight
4 AI Doctor Response – LLM generates professional advice
5 Doctor’s Voice Reply – Text-to-speech output for natural conversation
6 Modern UI – Built with Gradio (Login + Doctor Panel)

**Tech Stack**
1 Backend: Python, Gradio
2 AI Models: Whisper (speech-to-text), LLaMA/Groq (LLM), ElevenLabs TTS
3 Database: MySQL (user authentications
4 Others: dotenv, bcrypt

**Project Structure**
ai-doctor/
│── gradio_app.py          # Main Gradio app
│── authentication.py      # User auth functions
│── brain_of_the_doctor.py # Image analysis & LLM queries
│── voice_of_the_patient.py# Speech recognition
│── voice_of_the_doctor.py # Text-to-speech
│── config.py              # DB configs
│── .env                   # API keys & secrets

**User Flow**
1 Register/Login – Secure authentication with database.
2 Doctor Panel – Input via text, voice, or medical image.
3 AI Analysis – Speech-to-text, image analysis, and LLM-based medical response.
4 Doctor Response – Text + voice output.
5 Logout – Ends the session and returns to login page.

**Screenshots :**
a. <img width="1366" height="627" alt="image" src="https://github.com/user-attachments/assets/db7ed932-301b-4b29-ad81-4ccec3d554ce" />
b. <img width="1353" height="686" alt="image" src="https://github.com/user-attachments/assets/e859f0e6-bd0d-4aa6-aab5-34de785a6d6a" />
c. <img width="1286" height="653" alt="image" src="https://github.com/user-attachments/assets/58c9b09d-198a-4f54-8338-3db62074afb1" />


