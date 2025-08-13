# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel  
# from app.api.chat import get_response  

# app = FastAPI(title="Symptom Chatbot API")

# # Allow requests from frontend
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ChatRequest(BaseModel):
#     question: str

# class ChatResponse(BaseModel):
#     answer: str

# @app.post("/chat", response_model=ChatResponse)
# async def chat(request: ChatRequest):
#     try:
#         answer = get_response(request.question)
#         return ChatResponse(answer=answer)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.api.chat import get_response

app = FastAPI(title="Symptom Chatbot API")

# CORS setup for frontend connection
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    question: str
    age: int
    gender: str

# Response model
class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        answer = get_response(request.question, request.age, request.gender)
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

