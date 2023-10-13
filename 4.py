from fastapi import FastAPI
from transformers import pipeline
import uvicorn

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()

# Create a text summarization pipeline using Transformers
summarizer = pipeline("summarization")

@app.post("/summarize/")
async def summarize_text(input_text: dict):
    """
    Summarize a given text.
    :param input_text: {"text": "Your input text here"}
    :return: {"summary": "Generated summary here"}
    """
    text = input_text["text"]
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
    return {"summary": summary}
if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=5500)