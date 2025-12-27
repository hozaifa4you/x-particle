from metatrader.account_info import account_info
from langchain.tools import tool


@tool
def get_account_info_tool():
    """
    Retrieve the current MetaTrader 5 account information as a dictionary.

    Returns:
        dict: Account details with keys such as:
            - login (int): Account number
            - trade_mode (int): Trading mode
            - leverage (int): Account leverage
            - balance (float): Account balance
            - equity (float): Account equity
            - margin (float): Used margin
            - margin_free (float): Free margin
            - margin_level (float): Margin level
            - profit (float): Current profit/loss
            - name (str): Account type name
            - server (str): Server name
            - currency (str): Account currency
            - ... (other MetaTrader5 account fields)

    Example:
        {
            'login': 270709358, 'trade_mode': 0, 'leverage': 500, 'limit_orders': 1024,
            'margin_so_mode': 0, 'trade_allowed': True, 'trade_expert': True, 'margin_mode': 2,
            'currency_digits': 2, 'fifo_close': False, 'balance': 500.0, 'credit': 0.0, 'profit': -2.1,
            'equity': 497.9, 'margin': 0.0, 'margin_free': 497.9, 'margin_level': 0.0, 'margin_so_call': 60.0,
            'margin_so_so': 0.0, 'margin_initial': 0.0, 'margin_maintenance': 0.0, 'assets': 0.0, 'liabilities': 0.0,
            'commission_blocked': 0.0, 'name': 'Standard', 'server': 'Exness-MT5Trial17', 'currency': 'USD',
            'company': 'Exness Technologies Ltd'
        }
    """

    info = account_info()
    return info
