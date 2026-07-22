# Binance Futures Testnet Trading Bot

A simple Python Command Line Interface (CLI) trading bot for the Binance Futures Testnet.

## Features
- Connects to Binance Futures Testnet.
- Places **MARKET** orders.
- Places **LIMIT** orders.
- Validates all user inputs.
- Logs all activity (success and errors) to `logs/trading.log`.

## Project Structure
```text
trading_bot/
├── bot/
│   ├── __init__.py       # Makes bot a package
│   ├── client.py         # Binance connection logic
│   ├── orders.py         # Market and Limit order execution
│   ├── validators.py     # User input validation
│   └── logging_config.py # Log generation
├── logs/                 # Folder containing trading.log
├── cli.py                # Main program entry point
├── requirements.txt      # Project dependencies
└── .env                  # API Keys vault (hidden)
```

## Prerequisites
- Python 3 installed.
- Binance Futures Testnet API Key and Secret.

## Installation

1. Navigate to the project directory:
   ```bash
   cd trading_bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the `.env` file and insert Testnet keys:
   ```env
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_api_secret_here
   ```

## Usage

Run the bot from the command line:
```bash
python cli.py
```

Follow the on-screen prompts to select your order type, symbol (e.g., BTCUSDT), side, quantity, and price.

## Logs
Check `logs/trading.log` to see a detailed record of your trades and any errors.
