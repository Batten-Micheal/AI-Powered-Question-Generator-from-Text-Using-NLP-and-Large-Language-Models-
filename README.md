🤖 AI Question Generator
📌 Project Overview

The AI Question Generator is a beginner-friendly project that uses Natural Language Processing (NLP) and Large Language Models (LLMs) to automatically generate questions from a given paragraph.

The user provides a text passage, and the system generates:

Multiple-choice questions

Short-answer questions

Quiz-style questions

This tool can help students, teachers, and learners create quick quizzes from study material.

🎯 Objectives

Automatically generate questions from text.

Help students revise study notes through quizzes.

Demonstrate the use of LLMs in education.

Build a simple AI-powered web application.

🚀 Features

Input any paragraph or study notes.

Generate multiple questions automatically.

Supports:

Multiple-choice questions

Short-answer questions

Quiz-style questions

Simple web interface using Streamlit.

Fast and beginner-friendly implementation.

🧠 Technologies Used

Python

NLP (Natural Language Processing)

LLM API

Streamlit (for web interface)

Python Libraries

streamlit

python-dotenv

openai (or any LLM API)

Related fields:

Natural Language Processing

Machine Learning

📂 Project Structure
AI-Question-Generator
│
├── app.py              # Main Streamlit application
├── .env                # API key file
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Question-Generator.git
cd AI-Question-Generator
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create a .env file in the project folder.

OPENAI_API_KEY=your_api_key_here
5️⃣ Run the Application
streamlit run app.py

The app will open in your browser.

💡 How It Works

User enters a paragraph of text.

The system sends the text to an LLM model.

The AI analyzes the content.

The AI generates questions based on the text.

Questions are displayed on the web interface.

📊 Example

Input Paragraph

Machine learning is a branch of artificial intelligence that allows systems to learn from data and improve without being explicitly programmed.

Generated Questions

What is machine learning?

Which field does machine learning belong to?

How do machine learning systems improve over time?

📈 Future Improvements

Add PDF or document upload

Add automatic answer generation

Generate multiple-choice options

Save quizzes as PDF

Add difficulty levels

🎓 Learning Outcomes

Through this project you will learn:

Basics of LLM applications

Prompt engineering

Building simple AI web apps

Working with APIs and Python
