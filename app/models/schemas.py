from pydantic import BaseModel, EmailStr

class CodeRequest(BaseModel):
    code: str
    language: str

class CodeResponse(BaseModel):
    explanation: list
    errors: list
    suggestions: list
    
class User(BaseModel):
    email: EmailStr
    password: str