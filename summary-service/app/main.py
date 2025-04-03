from fastapi import FastAPI, Query
import openai
import os

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/summarize")
def summarize(text: str = Query(...)):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "請幫我摘要以下文字"},
                  {"role": "user", "content": text}]
    )
    return {"result": response.choices[0].message["content"]}
