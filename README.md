# AI-Driven-Mental-Health-Journaling-Companion
A conversational tool that assists users in journaling for mental health by providing empathetic responses, prompts for reflection, and mood tracking using an LLM.


## 📋 Overview

This application provides a simple yet powerful journaling experience where users can:
- Write daily journal entries about their thoughts and feelings
- Receive empathetic AI-generated responses using Google's Gemini model
- Review past entries and responses in chronological order
- Experience a calming, supportive interface for mental wellness

The AI companion responds with supportive and reflective comments, helping users process their emotions and gain new perspectives on their experiences.


## ✨ Features

- **Interactive Journaling**: Simple interface for writing and submitting journal entries
- **AI-Powered Responses**: Utilizes Google's Gemini API to generate empathetic, supportive responses
- **Entry History**: View all past journal entries and AI responses in reverse chronological order
- **Local Storage**: All entries are stored locally in a JSON file for privacy
- **Responsive Design**: Clean, calming interface that works on various screen sizes


## 🛠️ Technologies Used

- **Flask**: Python web framework for the backend
- **Google Gemini API**: Large Language Model API for generating AI responses
- **HTML/CSS**: Frontend interface
- **JSON**: Local data storage format


## 🚀 Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
2. **Create a .env file in the project root with your Gemini API key**
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here


## 💻 Usage
1. **Start the application**
   ```bash
   python app.py
2. Open your browser and navigate to http://127.0.0.1:5000/

3. Begin journaling by typing your thoughts in the text area and clicking submit

4. View history by clicking the "View Past Entries" link


## 📁 Project Structure
```
mental_health_journal/
│
├── app.py                # Main Flask application
├── templates/            # HTML templates
│   ├── index.html        # Main journal page
│   └── history.html      # Page to view past entries
├── static/               # Static files
│   └── style.css         # CSS styling
├── data/                 # Data storage
│   └── entries.json      # JSON file storing all entries
├── .env                  # Environment variables (not in version control)
└── requirements.txt      # Project dependencies
```

## ⚙️ Configuration
You can customize the AI behavior by modifying the prompt in app.py:
  ```python
  prompt = f"""
  You are a supportive mental health companion. Respond to the user's journal entry with empathy and kindness.
  Keep the response short (2-3 sentences), offer a gentle reflection or follow-up question, and avoid giving medical advice.
  User entry: {user_entry}
  """
```
Adjust this prompt to change the tone, length, or style of AI responses.

## 🔒 Privacy and Security
All journal entries are stored locally on your machine in the data/entries.json file
No data is sent to external servers except for the journal text sent to Google's Gemini API for response generation
Your Gemini API key is stored in the .env file which should not be committed to version control
