import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AccessLearn API",
    description="Assistive learning backend for visually and hearing-impaired students",
    version="0.1.0"
)

# Initialize Anthropic client for curriculum adaptation
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", "your_api_key_here"))

class LessonContent(BaseModel):
    title: str
    raw_text: str
    target_mode: str  # "screen_reader" for blind students or "simplified_captions" for deaf students

@app.get("/")
async def root():
    return {
        "project": "AccessLearn",
        "status": "active",
        "message": "Accessibility engine is running."
    }

@app.post("/api/v1/adapt-lesson")
async def adapt_lesson(content: LessonContent):
    """
    Adapts standard educational text into accessible formats for blind or deaf learners.
    """
    if content.target_mode == "screen_reader":
        system_prompt = (
            "You are an accessibility assistant for blind students. "
            "Convert the following lesson into a clear, linear, audio-friendly structure "
            "optimized for screen readers, avoiding visual-only references."
        )
    elif content.target_mode == "simplified_captions":
        system_prompt = (
            "You are an accessibility assistant for deaf and hard-of-hearing students. "
            "Convert the following lesson into structured, easy-to-follow visual notes "
            "with clear headings and key concept summaries."
        )
    else:
        raise HTTPException(status_code=400, detail="Invalid target_mode. Choose 'screen_reader' or 'simplified_captions'.")

    try:
        response = anthropic_client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=1500,
            system=system_prompt,
            messages=[
                {"role": "user", "content": f"Lesson Title: {content.title}\n\nContent:\n{content.raw_text}"}
            ]
        )
        return {
            "title": content.title,
            "mode": content.target_mode,
            "adapted_content": response.content[0].text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
