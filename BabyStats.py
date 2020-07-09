#%%
import requests
from credentials import credentials

class BabyStats: 

    def getBabyStats(self, eventName,babyName,eventTime):

        url = "https://www.babystats.org/api/public"

        payload = {
            "id": credentials['ids'],
            "accessToken": credentials['token'],
            "event": eventName,
            "babyName" : babyName,
            "eventTime" : eventTime
        }

        r = requests.request("POST", url, data = payload)

        return r.json()

