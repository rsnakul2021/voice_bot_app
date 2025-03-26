# VOICE BOT APPLICATION
====================

A web-based voice bot that uses speech recognition, ChatGPT, and text-to-speech to have interactive conversations. The bot responds based on personalized information and can speak its responses.

# PROJECT STRUCTURE
---------------
voice-bot/
├── app.py           # Local version using pyttsx3 (for development)
├── app_1.py         # Production version using gTTS (for deployment)
├── requirements.txt
├── personal_info.txt
├── .env
├── .gitignore
├── gunicorn_config.py
└── templates/
    └── index.html

# SETUP INSTRUCTIONS
----------------

1. LOCAL DEVELOPMENT
-------------------
a) Clone the repository and navigate to the folder
b) Create virtual environment using pipenv:
   pipenv install

c) Install dependencies:
   pip install -r requirements.txt

d) Create .env file with your OpenAI API key:
   OPENAI_API_KEY=your_openai_api_key_here

e) Update personal_info.txt with your information

f) Run local server:
   python app.py

2. DEPLOYMENT TO RENDER
----------------------
a) Create GitHub repository and push code:
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main

b) Go to Render.com:
   - Sign up/Login
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

c) Configure web service:
   - Name: voice-bot
   - Environment: Python
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app_1:app
   - Add Environment Variable:
     Key: OPENAI_API_KEY
     Value: Your OpenAI API key

d) Click "Create Web Service"

# USAGE
-----
1. Local Development:
   - Visit http://localhost:5000
   - Uses pyttsx3 for text-to-speech
   - Better for testing

2. Production (Render):
   - Visit your Render URL
   - Uses gTTS for text-to-speech
   - Suitable for sharing

3. Using the Voice Bot:
   - Click "Click to Record"
   - Allow microphone access
   - Speak your question
   - Wait for response
   - Response will be displayed and spoken

REQUIREMENTS
-----------
- Python 3.7+
- Modern web browser (Chrome/Edge recommended)
- Microphone access
- Internet connection
- OpenAI API key

TROUBLESHOOTING
--------------
1. Microphone issues:
   - Use HTTPS in production
   - Grant microphone permissions
   - Use Chrome/Edge browser

2. Speech recognition:
   - Speak clearly
   - Check background noise
   - Ensure good internet

3. Deployment:
   - Check Render logs
   - Verify environment variables
   - Check requirements.txt

# SECURITY NOTES
-------------
- Never commit .env file
- Keep API key secure
- Monitor API usage

For additional support or questions, contact: [Your contact information]
