from fastapi import APIRouter, Depends
from typing import List, Optional
from Common.entities import Teacher, Class
from Common.logger import Logger
from Common.auth import get_current_user

router = APIRouter()
logger = Logger("TeacherAPI")

@router.get("/")
def teacher_root():
    return {"message": "This is the v1 Teacher API root."}

@router.get("/me", response_model=Teacher)
def get_teacher_profile(current_user: dict = Depends(get_current_user)):
    logger.info(f"Accessed /me endpoint by user: {current_user.get('sub')}")
    return Teacher(
        id="t001",
        name="Ms. Smith",
        school_id="sch001",
        class_ids=["cls101"]
    )

@router.get("/me/classes", response_model=List[Class])
def get_teacher_classes(classid: Optional[str] = None, current_user: dict = Depends(get_current_user)):
    logger.info(f"Accessed /me/classes endpoint with classid={classid} by user: {current_user.get('sub')}")
    classes = [
        Class(
            id="cls101",
            school_id="sch001",
            name="Grade 10 - A",
            teacher_ids=["t001", "t002"],
            student_ids=["s101", "s102", "s103"]
        ),
        Class(
            id="cls102",
            school_id="sch001",
            name="Grade 9 - B",
            teacher_ids=["t001"],
            student_ids=["s104", "s105"]
        )
    ]
    if classid is not None:
        filtered = [c for c in classes if c.id == classid]
        logger.debug(f"Returning filtered classes: {filtered}")
        return filtered
    logger.debug(f"Returning all classes: {classes}")
    return classes 