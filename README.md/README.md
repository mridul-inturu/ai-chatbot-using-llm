# AI Chatbot Using LLMs

## 📌 Project Overview
This project is a full-stack AI Chatbot built using Large Language Models (LLMs).  
It allows users to interact with an AI through a web interface.

The backend is built using **FastAPI**, the frontend using **Streamlit**, and the AI responses are generated using **Groq LLM APIs**.


## 🛠️ Technologies Used
- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Groq LLM API
- Git & GitHub

## 📁 Project Structure
ai_chatbot_project

1. backend/
-main.py
-requirements.txt
-.env.example
2. frontend
-app.py
-requirements.txt
3. README.md

## How to Run the Project

### 1️⃣ Clone the Repository
git clone https://github.com/mridul-inturu/ai-chatbot-using-llm.git
cd ai-chatbot-using-llm


### 2️⃣ Backend Setup (FastAPI)

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create a `.env` file:
GROQ_API_KEY=your_api_key_here

Run the backend:
uvicorn main:app --reload

Backend runs at:
http://127.0.0.1:8000


### 3️⃣ Frontend Setup (Streamlit)

Open a **new terminal**:
cd frontend
pip install -r requirements.txt
streamlit run app.py

## 📄 Submission Notes
This project was developed as part of **Project 1 – AI Domain** under Coincent training.


## 👤 Author
**Mridul Inturu**