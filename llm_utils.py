# llm_utils.py
from openai import OpenAI
import os
import pandas as pd
from dotenv import load_dotenv
import httpx

load_dotenv()

def answer_question(query: str, data: pd.DataFrame) -> str:
    if data.empty:
        return "No market data available. Please run /ingest first."
    
    # Initialize client inside function to get fresh error messages
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OpenAI API key not found. Please set OPENAI_API_KEY environment variable."
    
    try:
        # Create a custom HTTP client without proxy settings
        http_client = httpx.Client(timeout=30.0)
        client = OpenAI(api_key=api_key, http_client=http_client)
    except Exception as e:
        return f"Failed to initialize OpenAI client: {str(e)}"

    # Simplify: Turn dataframe into a string
    summary = data.tail(3).to_string()

    prompt = f"""
    You are a financial assistant.
    The user asked: {query}
    Here is some recent market data:
    {summary}
    Answer concisely.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling OpenAI API: {str(e)}"
