from Data.GroupData import GroupData

from FW.API.APIBase import APIBase
from FW.API.ApiUser import ApiUser
from FW.FWBase import FWBase
from FW.WEB.MainPage import MainPage
from FW.WEB.Search import Search


class ApplicationManager:

    data = GroupData()

    def __init__(self):
        self.fw_base = FWBase(self)
        self.api_base = APIBase(self)
        self.api_user = ApiUser(self)

        self.web_main_page = MainPage(self)
        self.web_search = Search(self)
