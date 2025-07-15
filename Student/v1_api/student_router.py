from fastapi import APIRouter, Depends
from Common.entities import Student
from Common.auth import get_current_user
from Common.logger import Logger

router = APIRouter()
logger = Logger("StudentAPI")

@router.get("/me", response_model=Student)
def get_student_profile(current_user: dict = Depends(get_current_user)):
    logger.info(f"Accessed /me endpoint by user: {current_user.get('sub')}")
    # Mock student profile
    return Student(
        id="s101",
        name="John Doe",
        school_id="sch001",
        class_ids=["cls101", "cls102"]
    ) 