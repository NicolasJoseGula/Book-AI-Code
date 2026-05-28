from fastapi import FastAPI, Depends

def get_db():
    db = ... #Create Database session
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("user/{email}/messages")
def get_current_user_messages(email, db=Depends(get_db)):
    user = db.query(...) # db is reused
    messages = db.query(...) #db is reused
    return messages

