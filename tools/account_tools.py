from metatrader.account_info import account_info
from langchain.tools import tool


@tool
def get_account_info_tool():

    return account_info()
