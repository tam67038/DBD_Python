import logging
import os
from datetime import datetime, timedelta

LOG_DIR = "logs"
RETENTION_DAYS = 90

os.makedirs(LOG_DIR, exist_ok=True)

def cleanup_old_logs():
    cutoff = datetime.now() - timedelta(days=RETENTION_DAYS)

    for file in os.listdir(LOG_DIR):
        if file.startswith("app-") and file.endswith(".log"):
            try:
                date_str = file.replace("app-", "").replace(".log", "")
                file_date = datetime.strptime(date_str, "%Y-%m-%d")

                if file_date < cutoff:
                    os.remove(os.path.join(LOG_DIR, file))
            except:
                pass


def get_logger(name):

    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"app-{today}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    cleanup_old_logs()
    return logger