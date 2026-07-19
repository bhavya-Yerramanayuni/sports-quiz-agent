from google import genai
from src.config import GEMINI_API_KEY
from src.database import search_facts
from src.search import get_live_news

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_quiz(sport, difficulty):

    db_context = "\n".join(
        search_facts(
            sport,
            f"{sport} history records championships",
            n_results=3
        )
    )

    web_context = get_live_news(sport)

    prompt = f"""
You are an expert sports quiz creator.

Your task is to generate engaging, factually accurate multiple-choice quizzes.

STRICT RULES:

1. Use ONLY the provided context.
2. Never hallucinate.
3. Generate exactly FIVE questions.
4. Questions should NOT repeat the same fact.
5. Mix history, achievements, tournaments, records and recent news.
6. Difficulty level: {difficulty}
7. Make options realistic.
8. Only one option should be correct.

Historical Context:
{db_context}

Recent News:
{web_context}

Return in exactly this format:

Sport: {sport}
Difficulty: {difficulty}

Question 1:
Question:
A.
B.
C.
D.
Correct Answer:
Explanation:

Question 2:
Question:
A.
B.
C.
D.
Correct Answer:
Explanation:

Question 3:
Question:
A.
B.
C.
D.
Correct Answer:
Explanation:

Question 4:
Question:
A.
B.
C.
D.
Correct Answer:
Explanation:

Question 5:
Question:
A.
B.
C.
D.
Correct Answer:
Explanation:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text