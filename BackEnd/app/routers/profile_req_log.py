from fastapi import APIRouter
from app.services.profile_req_log_service import get_logs

router = APIRouter(
    prefix="/profile-log",
    tags=["ProfileReqLog"]
)

@router.get("/")
def search_logs(
    request_rgno: str = None,
    job_status: str = None
):
    return get_logs(request_rgno, job_status)