from fastapi import FastAPI
from app.views import user_view

app = FastAPI()

# รวม View เข้ากับ App
app.include_router(user_view.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI CRUD Project"}
