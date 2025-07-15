from fastapi import FastAPI, APIRouter, Form
from Admin.v1_api.admin_router import router as admin_v1_router
from Common.auth import create_access_token, verify_user_credentials

app = FastAPI()

auth_router = APIRouter()

@auth_router.post("/token")
def login_for_access_token(username: str = Form(...), password: str = Form(...)):
    user = verify_user_credentials(username, password)
    user_data = {"sub": username, "role": user["role"]}
    access_token = create_access_token(user_data)
    return {"access_token": access_token, "token_type": "bearer"}

app.include_router(auth_router)
app.include_router(admin_v1_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "TutoraHub LMS Admin API!"} 