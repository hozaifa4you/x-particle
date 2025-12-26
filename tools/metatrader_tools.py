from metatrader.metatrader import send_order, OrderRequest
from langchain.tools import tool


@tool
def send_order_tool(order_request: OrderRequest):
    return send_order(order_request)
