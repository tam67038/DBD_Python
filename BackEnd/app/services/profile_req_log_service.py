from sqlalchemy import text
from app.database import get_db
from app.logging_config import get_logger

logger = get_logger(__name__)

def get_logs(request_rgno=None, job_status=None):
    db = get_db()

    try:
        sql = """
            SELECT *
            FROM DBDApiV2.Profile_Req_Log
            WHERE 1=1
        """

        params = {}

        if request_rgno:
            sql += " AND RequestRgno = :rgno"
            params["rgno"] = request_rgno

        if job_status:
            sql += " AND JobStatus = :status"
            params["status"] = job_status

        logger.info(
            f"Get DBDApiV2.Profile_Req_Log with params={params}"
        )
        
        result = db.execute(text(sql), params)
        return result.mappings().all()
    
    except Exception as e:
        logger.error(
            f"Get logs failed error={str(e)}",
            exc_info=True
        )
        raise

    finally:
        db.close()
        
def check_status_Profile_Req_Log():
    db = get_db() 

    try:
        sql = """
            SELECT *
            FROM DBDApiV2.Profile_Req_Log
            WHERE TRIM(APIResponseCode) = '1000'
        """
        
        logger.info(
            f"Get DBDApiV2.Profile_Req_Log check_status"
        )
        
        result = db.execute(text(sql))
        return result.mappings().all()
    
    except Exception as e:
        logger.error(
            f"Get DBDApiV2.Profile_Req_Log check_status failed error={str(e)}",
            exc_info=True
        )
        raise

    finally:
        db.close()