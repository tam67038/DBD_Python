import json
import os
import base64
from app.models.InquirySHL_model import APIResponse
from app.logging_config import get_logger
from app.services.pdf_service import save_base64_to_pdf
from app.services.hash_service import calculate_sha256
from datetime import datetime

logger = get_logger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MOCK_PATH = os.path.join(BASE_DIR, "mock_data", "0107561000013.json")

def get_mock_bdex_response() -> APIResponse:
    try:
        with open(MOCK_PATH, "r", encoding="utf-8") as f:
            raw = json.load(f)

        model = APIResponse(**raw)

        logger.info("Load mock BDEX data success")
        return model

    except Exception as e:
        logger.error(f"Load mock BDEX failed: {str(e)}", exc_info=True)
        raise
    
def save_data():
    try:
        logger.info("Start save_data")
        resp = get_mock_bdex_response()
        saved_files = []

        for f in resp.data.list_of_file:
            logger.info(f"Processing file: {f.file_name}")
            try:
                file_bytes = base64.b64decode(f.result)
                hash_local = calculate_sha256(file_bytes)
                dt_str = datetime.now().strftime("%Y%m%d%H%M%S")

                if hash_local != f.hashes:
                    logger.error(
                        f"Hash mismatch file={f.file_name} "
                        f"api_hash={f.hashes} local_hash={hash_local}"
                    )
                    continue

                file_path = save_base64_to_pdf(
                    f.result,
                    resp.data.organization_juristic_id + "_" + dt_str + ".pdf"
                )
                logger.info(f"Save file success: {file_path}")
                saved_files.append(file_path)
                
            except Exception as file_err:
                logger.error(
                    f"Process file failed: {f.file_name} "
                    f"error={str(file_err)}",
                    exc_info=True
                )

        logger.info(f"Finish save_data, total_saved={len(saved_files)}")
        return saved_files
        
    except Exception as e:
        logger.error(f"Save file failed: {str(e)}", exc_info=True)
        raise
    