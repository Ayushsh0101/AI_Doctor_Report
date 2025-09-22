🩺 AI Doctor – Voice & Vision Assistant

An AI-powered healthcare assistant that allows patients to interact with doctors using voice and image inputs.
It uses speech recognition, image analysis, and an advanced language model to provide professional medical advice. The system also responds in doctor’s voice for a natural conversation flow.

✨ Features

🔐 User Authentication – Secure login & registration with hashed passwords

🎤 Speech-to-Text – Patients can speak their query, converted into text

🖼 Image Analysis – Upload medical images (like X-rays/skin images) for AI diagnosis

🤖 AI Doctor Response – LLM generates medical insights

🔊 Doctor’s Voice Reply – Text-to-speech for natural doctor conversation

🖥 Modern UI – Built with Gradio (Login + Doctor Panel)

🛠 Tech Stack

Backend: Python, Gradio

AI Models: Whisper (speech-to-text), LLaMA / Groq (LLM), ElevenLabs TTS

Database: MySQL (for user authentication)

Others: dotenv, bcrypt

📂 Project Structure
ai-doctor/
│── gradio_app.py          # Main Gradio app
│── authentication.py      # User auth functions
│── brain_of_the_doctor.py # Image analysis & LLM queries
│── voice_of_the_patient.py# Speech recognition
│── voice_of_the_doctor.py # Text-to-speech
│── config.py              # DB configs
│── .env                   # API keys & secrets

⚙️ Installation & Setup

Clone the repo

git clone https://github.com/your-username/ai-doctor.git
cd ai-doctor


Create virtual environment

python -m venv .venv
source .venv/bin/activate   # for Linux/Mac
.venv\Scripts\activate      # for Windows


Install dependencies

pip install -r requirements.txt


Set up .env file
Create a .env file in the project root and add:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=doctor_ai

ELEVENLABS_API_KEY=your_api_key
GROQ_API_KEY=your_api_key


Set up Database

CREATE DATABASE doctor_ai;
USE doctor_ai;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    email VARCHAR(100),
    phone VARCHAR(20),
    password VARCHAR(255)
);

▶️ How to Run

Run the Gradio app:

python gradio_app.py


It will start on:

http://127.0.0.1:7860/
