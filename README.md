# AI Poem Generator 🖋️✨

A web application that generates beautiful poems using OpenAI's GPT-3.5 model. Users can input any topic and receive an original 4-line poem.

## Features
- Generates unique poems on any topic
- Simple and intuitive web interface
- Fast response using OpenAI's API
- Secure API key management

## Technologies Used
- Python 3.x
- Flask (Web Framework)
- OpenAI API (GPT-3.5)
- HTML/CSS (Frontend)
- python-dotenv (Environment Variables)

## Installation

### Prerequisites
- Python 3.8+
- OpenAI API key (Get one [here](https://platform.openai.com/api-keys))
- Git (optional)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-poem-generator.git
   cd ai-poem-generator

   Create and activate virtual environment:
bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate  # Windows


Install dependencies:
bash
pip install -r requirements.txt

Create .env file:
OPENAI_API_KEY=your-api-key-here


Run the application:

bash
python app.py
Open your browser to:

text
http://localhost:5000
Enter a topic and click "Generate Poem"

Configuration
Modify app.py to change:

Poem length (lines)
Writing style (haiku, sonnet, etc.)
AI model (gpt-3.5-turbo or gpt-4)

Troubleshooting
API Key Errors: Verify .env file exists and contains valid key
Module Not Found: Reinstall requirements with pip install -r requirements.txt
Rate Limits: Check your OpenAI quota here
