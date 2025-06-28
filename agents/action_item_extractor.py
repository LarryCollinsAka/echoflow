import re
import requests
from settings import settings

def extract_action_items(summary: str) -> list[dict]:
    prompt = (
        "From the following meeting summary, extract clear action items. "
        "Each item should include: description, owner (if available), and due date (if mentioned). "
        f"\n\nMeeting Summary:\n{summary}"
    )

    response = requests.post(
        url=settings.GRANITE_SUMMARY_URL,
        headers={"Authorization": f"Bearer {settings.HF_API_KEY}"},
        json={"inputs": prompt},
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(f"Granite model error: {response.text}")

    result = response.json()
    return parse_action_items(result.get("generated_text", ""))


def parse_action_items(text: str) -> list[dict]:
    """
    Very simple parser that assumes the LLM returns one action item per line,
    optionally including an owner and due date.
    """
    items = []
    lines = text.strip().split("\n")
    for line in lines:
        if not line.strip():
            continue

        match = re.match(r"(?:- )?(.*?)(?: \(Owner: (.*?)\))?(?: \(Due: (.*?)\))?", line.strip())
        if match:
            description, owner, due_date = match.groups()
            items.append({
                "description": description.strip(),
                "owner": owner.strip() if owner else None,
                "due_date": due_date.strip() if due_date else None
            })

    return items