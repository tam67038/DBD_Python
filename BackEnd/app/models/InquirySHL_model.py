from pydantic import BaseModel, Field
from typing import List, Optional

class Status(BaseModel):
    code: str
    description: str

class FileInfo(BaseModel):
    doc_type: str = Field(..., alias="DocType")
    file_name: str = Field(..., alias="FileName")
    file_size: float = Field(..., alias="FileSize")
    number_of_page: int = Field(..., alias="NumberOfPage")
    mime_type: str = Field(..., alias="mimeType")
    hashes: str = Field(..., alias="Hashes")
    result: Optional[str] = Field(None, alias="Result")

    class Config:
        allow_population_by_field_name = True
        
class ResponseData(BaseModel):
    organization_juristic_id: str = Field(..., alias='OrganizationJuristicID')
    number_of_file: int = Field(..., alias='NumberOfFile')
    list_of_file: List[FileInfo] = Field(..., alias='ListOfFile')
    
    class Config:
        populate_by_name = True
        
class APIResponse(BaseModel):
    status: Status
    data: ResponseData