# agents/summarizer_agent.py

import requests
from settings import settings  # Centralized .env loader

def summarize_transcript(transcript: str, format: str = "bulleted") -> str:
    prompt = f"Summarize the following meeting transcript in {format} format:\n\n{transcript}"

    response = requests.post(
        url=settings.GRANITE_SUMMARY_URL,  # <- updated from app_config
        headers={"Authorization": f"Bearer {settings.HF_API_KEY}"},
        json={"inputs": prompt},
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"Granite model error: {response.text}")

    result = response.json()
    return result.get("generated_text", "").strip()