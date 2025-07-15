from fastapi import APIRouter, Depends
from typing import List
from Common.entities import School
from Common.auth import get_current_user
from Common.logger import Logger
from Common.roles import require_role

router = APIRouter()
logger = Logger("AdminAPI")

@router.get("/school", response_model=List[School])
def get_schools(current_user: dict = Depends(require_role("admin"))):
    logger.info(f"Accessed /v1/school by admin: {current_user.get('sub')}")
    # Mock data: return schools managed by this admin
    schools = [
        School(
            id="sch001",
            name="Greenwood High",
            address="123 Main St",
            admin_ids=[current_user.get('sub')]
        ),
        School(
            id="sch002",
            name="Lakeside Academy",
            address="456 Lake Ave",
            admin_ids=[current_user.get('sub')]
        )
    ]
    return schools 