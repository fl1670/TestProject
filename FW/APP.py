from Data.GroupData import GroupData

from FW.API.APIBase import APIBase
from FW.API.ApiUser import ApiUser
from FW.FWBase import FWBase


class ApplicationManager:

    data = GroupData()

    def __init__(self):
        self.fw_base = FWBase(self)
        self.api_base = APIBase(self)
        self.api_user = ApiUser(self)
