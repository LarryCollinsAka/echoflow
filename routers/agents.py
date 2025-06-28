# routers/agents.py

from fastapi import APIRouter
from pydantic import BaseModel
from agents.summarizer_agent import summarize_transcript
from agents.action_item_extractor import extract_action_items

router = APIRouter()

class SummaryRequest(BaseModel):
    transcript: str
    format: str = "bulleted"

@router.post("/agents/summarize")
def summarize(req: SummaryRequest):
    summary = summarize_transcript(req.transcript, req.format)
    return {"summary": summary}

class ActionItemRequest(BaseModel):
    summary: str

@router.post("/agents/actions")
def extract_actions(req: ActionItemRequest):
    items = extract_action_items(req.summary)
    return {"actions": items}

