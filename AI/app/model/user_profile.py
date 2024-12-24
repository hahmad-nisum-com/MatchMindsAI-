from pydantic import BaseModel
from typing import List, Optional

class Experience(BaseModel):
    company: str
    tenure: str

class UserProfile(BaseModel):
    name: str
    email: str
    skills:Optional[List[str]]=None
    tech_stack: Optional[List[str]]=None
    certifications: Optional[List[str]] = None
    experience: List[Experience]
    total_experience: float
    education: Optional[List[str]]=None
