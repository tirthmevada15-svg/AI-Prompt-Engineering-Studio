import requests
import streamlit as st

API_KEY = st.secrets["OPENROUTER_API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def call_llama(prompt):

    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]


def generate_magic_prompt(title):

    prompt = f"""
You are an expert prompt engineer.

Convert this TITLE into a professional AI prompt.

Title: {title}

Include:
Role
Context
Instructions
Tone
Output format
"""

    return call_llama(prompt)


def improve_prompt(prompt):

    instruction = f"""
Improve the following AI prompt to make it clearer and more powerful.

Prompt:
{prompt}
"""

    return call_llama(instruction)


def analyze_prompt(prompt):

    instruction = f"""
Evaluate this prompt.

Return:
Prompt Quality Score (0-100)
Strengths
Weaknesses
Suggestions

Prompt:
{prompt}
"""

    return call_llama(instruction)