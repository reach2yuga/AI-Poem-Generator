from flask import Flask, render_template, request
from openai import OpenAI  # Updated import
from dotenv import load_dotenv
import os

load_dotenv()  # Load API key from .env

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # New OpenAI client

@app.route("/", methods=["GET", "POST"])
def home():
    poem = ""
    if request.method == "POST":
        topic = request.form["topic"]
        response = client.chat.completions.create(  # Updated syntax
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poetic assistant."},
                {"role": "user", "content": f"Write a 4-line poem about {topic}."}
            ]
        )
        poem = response.choices[0].message.content  # Updated access to response
    return render_template("index.html", poem=poem)

if __name__ == "__main__":
    app.run(debug=True)