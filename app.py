from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os
from gtts import gTTS
import base64
import io

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load personal information
def load_personal_info(file_path="personal_info.txt"):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "You are a helpful AI assistant that answers questions about the user."

PERSONAL_INFO = load_personal_info()
conversation_history = [{"role": "system", "content": PERSONAL_INFO}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-text', methods=['POST'])
def process_text():
    try:
        # Get text from the request
        data = request.get_json()
        text = data.get('text', '')

        # Get ChatGPT response
        conversation_history.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history
        )
        response_text = response.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": response_text})

        # Convert response to speech using gTTS
        tts = gTTS(text=response_text, lang='en')
        audio_io = io.BytesIO()
        tts.write_to_fp(audio_io)
        audio_data = base64.b64encode(audio_io.getvalue()).decode()

        return jsonify({
            'success': True,
            'text': text,
            'response': response_text,
            'audio': audio_data,
            'audio_type': 'audio/mp3'  # gTTS produces MP3 files
        })

    except Exception as e:
        print(f"Error: {str(e)}")  # For debugging
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Using different port from original app
