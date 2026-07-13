import os
from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables
load_dotenv()


# Get Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")


# Configure Gemini
genai.configure(api_key=API_KEY)


# Select Gemini model
model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_learning_support(problem, emotion):
    """
    Generates personalized learning guidance
    based on student's problem and emotion.
    """

    prompt = f"""
    You are an AI Learning Support Assistant.

    Student Emotion:
    {emotion}

    Student Problem:
    {problem}

    Provide:
    1. Empathetic response
    2. Explanation strategy
    3. Learning tips
    4. Next steps

    Keep the response simple and motivating.
    """


    response = model.generate_content(prompt)

    return response.text



def regenerate_response(problem, emotion):
    """
    Generates a new response when user requests regeneration.
    """

    return generate_learning_support(
        problem,
        emotion
    )