from metatrader.account_info import account_info, terminal_info, allow_trading
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


@tool
def get_terminal_info_tool():
    """
    Retrieve the current MetaTrader 5 terminal (platform) information as a dictionary.

    Returns:
        dict: Terminal details with keys such as:
            - community_account (bool)
            - community_connection (bool)
            - dlls_allowed (bool)
            - trade_allowed (bool)
            - tradeapi_disabled (bool)
            - email_enabled (bool)
            - ftp_enabled (bool)
            - notifications_enabled (bool)
            - mqid (str)
            - build (int)
            - version (str)
            - language (str)
            - path (str)
            - ... (other MetaTrader5 terminal fields)

    Example:
        {
            'community_account': True,
            'community_connection': True,
            'dlls_allowed': True,
            'trade_allowed': True,
            'tradeapi_disabled': False,
            'email_enabled': False,
            'ftp_enabled': False,
            'notifications_enabled': False,
            'mqid': '...',
            'build': 3550,
            'version': '5.0.0.3550',
            'language': 'English',
            'path': 'C:/Program Files/MetaTrader 5',
            ...
        }
    """

    info = terminal_info()
    return info


@tool
def is_trading_allowed_tool():
    """
    Check if trading is currently allowed in the MetaTrader 5 terminal/account.

    Returns:
        dict: {'trading_allowed': True/False, 'message': str}
    Example:
        {'trading_allowed': True, 'message': 'Trading is allowed today.'}
    """

    info = allow_trading()
    return info
