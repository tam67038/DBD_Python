import base64
import os
from app.logging_config import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = r"D:\download"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_base64_to_pdf(base64_str: str, filename: str) -> str:
    try:
        file_bytes = base64.b64decode(base64_str)

        file_path = os.path.join(OUTPUT_DIR, filename)

        with open(file_path, "wb") as f:
            f.write(file_bytes)

        logger.info(f"Save PDF success: {file_path}")
        return file_path

    except Exception as e:
        logger.error(f"Save PDF failed: {str(e)}", exc_info=True)
        raise