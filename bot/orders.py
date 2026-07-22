from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderManager:
    def __init__(self):
        self.binance = BinanceClient()

    def place_market_order(self, symbol: str, side: str, quantity: float):
        """Places a MARKET order (buys/sells immediately at current price)."""
        logger.info(f"Attempting MARKET {side} for {quantity} {symbol}")
        try:
            response = self.binance.client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"MARKET order successful! Order ID: {response['orderId']}")
            return response
        except Exception as e:
            logger.error(f"MARKET order failed: {e}")
            return None

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float):
        """Places a LIMIT order (buys/sells only at the price you specify)."""
        logger.info(f"Attempting LIMIT {side} for {quantity} {symbol} at price {price}")
        try:
            response = self.binance.client.new_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"LIMIT order successful! Order ID: {response['orderId']}")
            return response
        except Exception as e:
            logger.error(f"LIMIT order failed: {e}")
            return None
