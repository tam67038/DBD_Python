from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProfileReqLogBase(BaseModel):
    RequestNo: str
    RequestRgno: str
    RequestDate: Optional[datetime]
    RequestBy: str
    RequestDesc: Optional[str]
    RequestAPICode: Optional[str]
    ResposeDatetime: Optional[datetime]
    APIResponseCode: Optional[str]
    APIResponseDescription: Optional[str]
    Cost: Optional[float]
    CallbackURL: Optional[str]
    JobID: Optional[str]
    JobStatus: Optional[str]

    class Config:
        orm_mode = True