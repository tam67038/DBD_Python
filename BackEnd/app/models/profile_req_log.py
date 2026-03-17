from sqlalchemy import Column, String, DateTime, Numeric
from app.database import Base

class ProfileReqLog(Base):
    __tablename__ = "Profile_Req_Log"
    __table_args__ = {"schema": "DBDApiV2"}

    RequestNo = Column(String(255), primary_key=True)
    RequestRgno = Column(String(15), nullable=False)
    RequestDate = Column(DateTime)
    RequestBy = Column(String(5), nullable=False)
    RequestDesc = Column(String(200))
    RequestAPICode = Column(String(255))
    ResposeDatetime = Column(DateTime)
    APIResponseCode = Column(String(255))
    APIResponseDescription = Column(String(255))
    Cost = Column(Numeric(19, 4))     # money
    CallbackURL = Column(String(255))
    JobID = Column(String(255))
    JobStatus = Column(String(255))