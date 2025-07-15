from typing import List
from pydantic import BaseModel

class Class(BaseModel):
    id: str
    school_id: str
    name: str
    teacher_ids: List[str]
    student_ids: List[str]

class Teacher(BaseModel):
    id: str
    name: str
    school_id: str
    class_ids: List[str]

class Student(BaseModel):
    id: str
    name: str
    school_id: str
    class_ids: List[str]

class School(BaseModel):
    id: str
    name: str
    address: str
    admin_ids: List[str] 