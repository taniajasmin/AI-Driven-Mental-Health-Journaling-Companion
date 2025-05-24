import os
import json
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Retrieve Gemini API key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in the .env file.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Set up the Gemini model (e.g., gemini-1.5-flash or gemini-1.5-pro)
model = genai.GenerativeModel('gemini-1.5-flash')

# Path to store journal entries locally (JSON for simplicity)
DATA_FILE = os.path.join('data', 'entries.json')
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Function to load journal entries
def load_entries():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Function to save journal entries
def save_entry(entry):
    entries = load_entries()
    entries.append(entry)
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f, indent=2)

# Route for the main journal page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_entry = request.form.get('entry')
        if user_entry:
            # Generate a prompt for Gemini to respond empathetically
            prompt = f"""
            You are a supportive mental health companion. Respond to the user's journal entry with empathy and kindness.
            Keep the response short (2-3 sentences), offer a gentle reflection or follow-up question, and avoid giving medical advice.
            User entry: {user_entry}
            """
            try:
                # Call Gemini API to generate response
                response = model.generate_content(prompt)
                ai_response = response.text
            except Exception as e:
                ai_response = "I'm sorry, I couldn't process your entry right now. Please try again."
                print(f"Gemini API Error: {e}")

            # Save entry with timestamp (simplified mood tracking can be added later)
            from datetime import datetime
            entry_data = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'user_entry': user_entry,
                'ai_response': ai_response
            }
            save_entry(entry_data)
            return redirect(url_for('index'))
    return render_template('index.html', entries=load_entries())

# Route to view history of entries
@app.route('/history')
def history():
    # entries = load_entries()
    # print("History Entries:", entries)
    return render_template('history.html', entries=load_entries())

if __name__ == '__main__':
    app.run(debug=True)