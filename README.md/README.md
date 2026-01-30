# AI Chatbot using Groq LLM

This project is a simple AI chatbot application built using **FastAPI** for the backend and **Streamlit** for the frontend.  
The chatbot uses **Groq’s LLM API** to generate intelligent responses.

---

## Technologies Used
- Python 3.10+
- FastAPI
- Uvicorn
- Streamlit
- Groq API
- Requests
- python-dotenv

---

## Project Structure
# AI Chatbot using Groq LLM

This project is a simple AI chatbot application built using **FastAPI** for the backend and **Streamlit** for the frontend.  
The chatbot uses **Groq’s LLM API** to generate intelligent responses.

---

## Technologies Used
- Python 3.10+
- FastAPI
- Uvicorn
- Streamlit
- Groq API
- Requests
- python-dotenv

---

## Project Structure
ai_chatbot_project/
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ ├── .env.example
│
├── frontend/
│ ├── app.py
│ ├── requirements.txt
│
├── README.md

## Backend Setup

1. Open a terminal and go to backend folder:
```bash
cd backend
Create and activate virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in backend folder and add:

ini
Copy code
GROQ_API_KEY=your_groq_api_key_here
Run backend server:

bash
Copy code
uvicorn main:app --reload
Backend will run at:

cpp
Copy code
http://127.0.0.1:8000
Frontend Setup
Open a new terminal and go to frontend folder:

bash
Copy code
cd frontend
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run Streamlit app:

bash
Copy code
streamlit run app.py
Frontend will open in the browser automatically.

How It Works
User enters a message in the Streamlit UI

Frontend sends request to FastAPI backend

Backend calls Groq LLM API

AI response is returned and displayed in UI

Note on Model Knowledge Cutoff
The AI model has a fixed training data cutoff (December 2023).
This is a standard limitation of large language models and does not affect application functionality.

Security Note
.env file is not included for security reasons

Each user must provide their own Groq API key