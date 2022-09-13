import datetime
import logging
import os
import sdm_service
import base64


utc_date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
ACCESS_KEY = "{}:{}:{}:{}".format(os.getenv("RUN_ID"), os.getenv("RANDOM_KEY_JOB_NAME"), os.getenv("RANDOM_KEY"), utc_date)
SECRET_KEY = base64.b64encode(os.getenv("SECRET").encode())
REQUIRED_ENV_VARS = ["SDM_ACCOUNT_ID", "RUN_ID", "RANDOM_KEY_JOB_NAME", "RANDOM_KEY", "SECRET", "SERVER_HOST"]

for env_var in REQUIRED_ENV_VARS:
    if not os.getenv(env_var):
        raise Exception(f'Missing required environment variable "{env_var}"')

account_id = os.getenv("SDM_ACCOUNT_ID")
service = sdm_service.create_sdm_service(ACCESS_KEY, SECRET_KEY, logging)
service.delete_account(account_id)
print("Account deleted successfully")
