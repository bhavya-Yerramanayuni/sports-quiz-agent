# AI-Powered Sports Quiz Generation Agent

## Project Overview

The AI-Powered Sports Quiz Generation Agent is a Retrieval-Augmented Generation (RAG) application that automatically generates engaging, factually accurate sports multiple-choice quizzes for social media.

The application combines:
- Historical sports knowledge stored in ChromaDB
- Live sports information retrieved through DuckDuckGo Search
- Google Gemini LLM for intelligent quiz generation

This approach minimizes hallucinations by grounding quiz generation using retrieved information.

---

## Features

- Select Sport (Cricket, Football, Tennis, Badminton, Basketball)
- Select Difficulty (Easy, Medium, Hard)
- Generate 5 Multiple Choice Questions
- Regenerate New Quiz
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- Live Web Search using DuckDuckGo
- Google Gemini Integration
- Interactive Streamlit Dashboard

---

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- DuckDuckGo Search
- Sentence Transformers

---

## Project Structure

```
sports-quiz-agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── sports_facts.json
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── generator.py
│   └── search.py
│
└── chroma_db/
```

---

## How It Works

1. User selects a sport.
2. User selects difficulty.
3. Historical sports facts are retrieved from ChromaDB.
4. Recent sports information is retrieved using DuckDuckGo Search.
5. Both contexts are combined into a single prompt.
6. Google Gemini generates factually grounded quiz questions.
7. Quiz is displayed in the Streamlit dashboard.

---

## RAG Architecture

```
User Input
      │
      ▼
Streamlit Dashboard
      │
      ▼
Retrieve Historical Facts
      │
      ▼
ChromaDB Vector Database
      │
      ▼
Retrieve Latest Sports News
      │
      ▼
DuckDuckGo Search
      │
      ▼
Combine Retrieved Context
      │
      ▼
Google Gemini
      │
      ▼
Generate Sports Quiz
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd sports-quiz-agent
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## Sample Output

- Sport Name
- Difficulty Level
- Five Multiple Choice Questions
- Four Options
- Correct Answer
- Explanation

---

## Future Improvements

- JSON formatted responses
- Better UI for quiz cards
- Score tracking
- More sports categories
- User authentication
- Quiz export as PDF

---

## Demo Video

Screen Recording:
https://drive.google.com/file/d/1NmigRK-Jxd5Fzn2-WRGCZcujNCf5LTse/view?usp=sharing

## GitHub Repository

https://github.com/bhavya-Yerramanayuni/sports-quiz-agent