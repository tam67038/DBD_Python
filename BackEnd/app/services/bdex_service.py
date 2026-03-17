import base64
import requests
from app.config import (
    BDEX_CONSUMER_KEY,
    BDEX_CONSUMER_SECRET,
    BDEX_TOKEN_URL,
    CREATE_JOB_URL
)
from app.logging_config import get_logger

logger = get_logger(__name__)

def get_bdex_token():

    try:
        logger.info("Requesting BDEX token")
        raw = f"{BDEX_CONSUMER_KEY}:{BDEX_CONSUMER_SECRET}"

        # encoded = base64.b64encode(raw.encode("utf-8")).decode("utf-8")
        encoded = "Ylh5NzReSWVtcTA9OnEwTDhAcnkmR2o4cw=="
        
        headers = {
            "Authorization": f"Basic {encoded}",
            "Content-Type": "application/json"
        }

        body = {
            "grant_type": "client_credentials"
        }

        res = requests.post(
            BDEX_TOKEN_URL,
            json=body,
            headers=headers,
            timeout=10
        )

        res.raise_for_status()
        logger.info("Get token success")
        result = res.json()

        logger.info(
            f"CreateJob API response status={res.status_code} "
            f"body={result}"
        )

        return res.json()["data"]
    
    except requests.exceptions.Timeout as e:
        logger.error("BDEX Token API timeout", exc_info=True)
        raise Exception("BDEX Token API timeout")

    except requests.exceptions.HTTPError as e:
        logger.error(
            f"BDEX Token API HTTP error: {e.response.text}",
            exc_info=True
        )
        raise Exception(f"BDEX Token API error: {e.response.text}")

    except Exception as e:
        logger.error(
            f"BDEX Token Unknown error: {str(e)}",
            exc_info=True
        )
        raise Exception(f"BDEX Token Unknown error: {str(e)}")
        
# -------------------------------
# สร้าง Job
# -------------------------------
def create_shareholder_image_job(org_id: str, callback_url: str):

    try:
        token = get_bdex_token()

        headers = {
            "Authorization": f"{token['tokenType']} {token['accessToken']}",
            "Content-Type": "application/json"
        }

        body = {
            "OrganizationJuristicID": org_id,
            "CallbackURL": callback_url
        }

        res = requests.post(
            CREATE_JOB_URL,
            json=body,
            headers=headers,
            timeout=10
        )

        res.raise_for_status()
        
        result = res.json()
        logger.info(
            f"CreateJob API response status={res.status_code} "
            f"requests={body} "
            f"body={result}"
        )
        
        return res.json()
    
    except requests.exceptions.Timeout as e:
        logger.error("CreateJob API timeout", exc_info=True)
        raise Exception("CreateJob API timeout")

    except requests.exceptions.HTTPError as e:
        logger.error(
            f"CreateJob API HTTP error:: {e.response.text}",
            exc_info=True
        )
        raise Exception(f"CreateJob API error:: {e.response.text}")

    except Exception as e:
        logger.error(
            f"CreateJob Unknown error: {str(e)}",
            exc_info=True
        )
        raise Exception(f"CreateJob Unknown error: {str(e)}")