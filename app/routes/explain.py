from fastapi import APIRouter, HTTPException
from app.models.schemas import CodeRequest, CodeResponse
from app.services.analyzer import analyze_code
from app.database.connection import explanations_collection
from datetime import datetime
from database.connection import users_collection


router = APIRouter()

@router.post("/explain")
def explain_code(data: CodeRequest):

    result = analyze_code(data.code, data.language)

    document = {
        "user_id": "demo_user",  # temporary
        "code": data.code,
        "explanation": result["explanation"],
        "errors": result["errors"],
        "suggestions": result["suggestions"],
        "created_at": datetime.utcnow()
    }

    explanations_collection.insert_one(document)

    return result

@router.get("/history/{user_id}")
def get_history(user_id: str):
    history = []

    for doc in explanations_collection.find({"user_id": user_id}):
        doc["_id"] = str(doc["_id"])
        history.append(doc)

    return history

from app.database.connection import users_collection
from fastapi import HTTPException

@router.post("/register")
def register_user(user: UserRegister):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    users_collection.insert_one({
        "email": user.email,
        "password": user.password  # ⚠ plain for now (we hash later)
    })

    return {"message": "User registered successfully"}