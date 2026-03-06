"""
AI Question Generator - Flask Backend
=====================================
A simple web app that takes a paragraph and generates quiz questions using Google Gemini.
"""

import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env file (so you can store GEMINI_API_KEY there)
load_dotenv()

# Create the Flask application
app = Flask(__name__)

# Configure Gemini with your API key (from .env or environment)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))


@app.route("/")
def index():
    """
    Homepage route - serves the main HTML page with the form.
    """
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_questions():
    """
    API route that receives the paragraph and returns generated questions.
    Called when the user clicks "Generate Questions".
    """
    # Get the paragraph from the form data sent by the frontend
    data = request.get_json()
    paragraph = data.get("paragraph", "").strip()

    # Validate that we have something to work with
    if not paragraph:
        return jsonify({"error": "Please enter a paragraph first."}), 400

    # Check if API key is set
    if not os.environ.get("GEMINI_API_KEY"):
        return jsonify({
            "error": "Gemini API key not set. Please set GEMINI_API_KEY in your .env file or environment."
        }), 500

    # Build the prompt that tells the LLM what to generate
    prompt = f"""Based on the following paragraph, generate quiz questions.

Paragraph:
{paragraph}

Generate the questions in this exact format. Use "===" to separate sections.

=== MULTIPLE CHOICE ===
1. [Question text]
   A) [Option A]
   B) [Option B]
   C) [Option C]
   D) [Option D]
   Correct: [A/B/C/D]

2. [Question text]
   A) [Option A]
   B) [Option B]
   C) [Option C]
   D) [Option D]
   Correct: [A/B/C/D]

3. [Question text]
   A) [Option A]
   B) [Option B]
   C) [Option C]
   D) [Option D]
   Correct: [A/B/C/D]

=== SHORT ANSWER ===
4. [Question 1]
5. [Question 2]
6. [Question 3]
"""

    try:
        # Use Gemini to generate questions (gemini-1.5-flash is fast and free-tier friendly)
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction="You are a helpful teacher. Generate clear quiz questions based on the given text. Format your response exactly as requested.",
        )
        response = model.generate_content(prompt, generation_config={"temperature": 0.7})

        # Get the generated text from Gemini's response
        generated_text = response.text

        # Return the questions to the frontend
        return jsonify({"questions": generated_text})

    except Exception as e:
        error_msg = str(e)
        # Show a friendly message for quota/rate limit errors
        if "429" in error_msg or "quota" in error_msg.lower() or "resource_exhausted" in error_msg.lower():
            return jsonify({
                "error": "Gemini API quota exceeded. Check your usage at https://aistudio.google.com/app/apikey"
            }), 503
        return jsonify({"error": error_msg}), 500


# Run the app when this file is executed directly (python app.py)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
