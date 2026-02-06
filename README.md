# 🤖 Agentic AI Research Assistant

An autonomous AI agent that plans, searches, summarizes, and stores research papers automatically using tool-based reasoning.

Built as part of the campus recruitment assignment for Cerevyn Solutions Pvt. Ltd.

---

## 🚀 Problem Statement

Build an Agentic AI system that can:

• Accept a user goal  
• Plan task steps  
• Use tools (search, summarize, store)  
• Maintain memory  
• Produce structured output  

### Example Goal
> Find top 3 recent AI research papers on agriculture and summarize them.

---

## 🧠 Solution Overview

This project implements a **task-oriented autonomous agent** that:

1. Plans execution steps  
2. Searches research papers using arXiv API  
3. Summarizes paper content  
4. Stores results in JSON  
5. Returns structured response  

The system works fully automatically with minimal user input.

---

## 🏗️ Architecture

User Goal  
↓  
Planner  
↓  
Search Tool (arXiv API)  
↓  
Summarizer Tool  
↓  
Memory  
↓  
Storage (JSON)  
↓  
Response  

---

## 🛠️ Tech Stack

• Python  
• FastAPI  
• arXiv API  
• REST APIs  
• JSON Storage  
• Modular Agent Design  

---

## 📁 Project Structure

agentic-ai/
│
├── main.py # FastAPI server
├── agent.py # Agent orchestration logic
├── planner.py # Task planning
│
├── tools/
│ ├── search_tool.py # Paper search (arXiv)
│ ├── summarize_tool.py
│ └── storage_tool.py
│
├── memory/
│ └── memory_store.py
│
└── output/
└── results.json # Generated output


---

## ⚙️ Setup & Run

### 1️⃣ Install dependencies

pip install fastapi uvicorn requests beautifulsoup4


### 2️⃣ Start server
uvicorn main:app --reload

### 3️⃣ Open browser
http://127.0.0.1:8000/docs


### 4️⃣ Test API
POST `/run-agent`

{
"goal": "Find top 3 recent AI research papers on agriculture"
}

---

## 📤 Sample Output

[
{
"title": "Paper Title",
"summary": "Short summary...",
"link": "http://arxiv.org/
..."
}
]


Saved automatically in:

output/results.json


---

## ✅ Features Implemented

✔ Task decomposition (planning)  
✔ Tool usage (search, summarize, store)  
✔ Memory management  
✔ Autonomous workflow  
✔ FastAPI backend  
✔ Structured output  

---

## 🎯 Highlights

• Fully autonomous AI agent  
• Real-time research paper retrieval  
• Clean modular architecture  
• Extensible for LLM / LangChain / vector DB  
• Production-style backend  

---

## 🚀 Future Improvements

• OpenAI/LLM summarization  
• Vector database memory (FAISS)  
• LangGraph orchestration  
• Web UI dashboard  
• Database storage  

---

## 👩‍💻 Author

Anjali  
B.Tech CSE (AI/ML)  
Agentic AI Internship Project