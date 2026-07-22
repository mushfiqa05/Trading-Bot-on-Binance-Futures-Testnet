import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures
from bot.logging_config import setup_logger

load_dotenv()

logger = setup_logger()

class BinanceClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        
        try:
            self.client = UMFutures(
                key=api_key, 
                secret=api_secret, 
                base_url="https://testnet.binancefuture.com"
            )
            self.client.ping()
            logger.info("Successfully connected to Binance Testnet!")
            
        except Exception as e:
            logger.error(f"Failed to connect to Binance: {e}")
