from fastapi import APIRouter, HTTPException
from app.services.bdex_service import get_bdex_token, create_shareholder_image_job

router = APIRouter(prefix="/bdex", tags=["BDEX"])

@router.get("/token")
def request_token():
    return get_bdex_token()

@router.post("/shareholder-image")
def create_job(org_id: str):
    try:
        return create_shareholder_image_job(
            org_id,
            "https://your-system.com/callback"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))