from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from utils.responses import get_response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    reply = get_response(user_message)
    return {"response": reply}
