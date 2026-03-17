from fastapi import APIRouter, HTTPException
from app.services.InquirySHL_service import save_data

router = APIRouter(prefix="/InquirySHL", tags=["InquirySHL"])

@router.post("/SavePDF")
def save_pdf():
    try:
        path = save_data()
        return {
            "status": "success",
            "file_path": path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))