# Copied from: https://github.com/strongdm/accessbot/blob/main/plugins/sdm/lib/service/sdm_service.py
import strongdm
import os


def create_sdm_service(api_access_key, api_secret_key, log):
    client = strongdm.Client(
        api_access_key,
        api_secret_key,
        host=os.getenv("SERVER_HOST"),
        insecure=True
    )
    return SdmService(client, log)


class SdmService:
    def __init__(self, client, log):
        self.__client = client
        self.__log = log
    
    def delete_account(self, id):
        """
        Creates a service account
        """
        try:
            self.__log.debug("##SDM## SdmService.delete_account")
            self.__client.accounts.delete(id)
        except Exception as ex:
            raise Exception("Delete account failed: " + str(ex)) from ex
        return True
