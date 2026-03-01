from pydantic import BaseModel, EmailStr

class CodeRequest(BaseModel):
    user_id: str
    code: str
    language: str

class CodeResponse(BaseModel):
    explanation: list
    errors: list
    suggestions: list
    
class User(BaseModel):
    email: EmailStr
    password: str
    
class UserRegister(User):
    pass

class UserLogin(BaseModel):
    email: EmailStr
    password: str