from pydantic import BaseModel, Field, EmailStr, field_validator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class UserCreate(BaseModel):
    username: str
    password: str

    # @validator('password') Esta version es vieja
    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit.')
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter')
        return value
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # En producción, restringir al dominio real
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/user")
async def create_user_controller(user: UserCreate):
    return {"name": user.username, "message":"Account successfully created"}