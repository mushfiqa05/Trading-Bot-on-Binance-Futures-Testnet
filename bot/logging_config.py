import logging
from pathlib import Path

def setup_logger():
    Path("logs").mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/trading.log"), 
            logging.StreamHandler() 
        ]
    )
    
    logger = logging.getLogger("TradingBot")
    return logger
