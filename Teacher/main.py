from fastapi import FastAPI, APIRouter, Form
from Teacher.v1_api.teacher_router import router as teacher_v1_router
from Common.logger import Logger
from fastapi import Depends
from fastapi.responses import JSONResponse
from Common.auth import create_access_token, verify_user_credentials

app = FastAPI()
logger = Logger("TeacherAPI")
auth_router = APIRouter()

@auth_router.post("/token")
def login_for_access_token(username: str = Form(...), password: str = Form(...)):
    user = verify_user_credentials(username, password)
    user_data = {"sub": username, "role": user["role"]}
    access_token = create_access_token(user_data)
    return {"access_token": access_token, "token_type": "bearer"}

app.include_router(auth_router)
app.include_router(teacher_v1_router, prefix="/v1/teacher")

@app.get("/")
def read_root():
    return {"message": "TutoraHub LMS Teacher API!"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 