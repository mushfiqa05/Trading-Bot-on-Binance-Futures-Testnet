import sys
from bot.orders import OrderManager
from bot.validators import validate_side, validate_quantity, validate_price

def main():
    print("=== Binance Futures Testnet Trading Bot ===")
    
    try:
        order_manager = OrderManager()
    except Exception as e:
        print(f"Failed to start bot: {e}")
        sys.exit(1)

    while True:
        print("\nOptions: 1) Market Order 2) Limit Order 3) Exit")
        choice = input("Select an option (1/2/3): ").strip()

        if choice == '3':
            print("Exiting...")
            break

        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        # Get Inputs
        symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
        
        side = input("Enter side (BUY / SELL): ").strip().upper()
        if not validate_side(side):
            print("Error: Invalid side. Must be BUY or SELL.")
            continue

        quantity = input("Enter quantity (e.g., 0.001): ").strip()
        if not validate_quantity(quantity):
            print("Error: Invalid quantity. Must be a positive decimal.")
            continue
        
        quantity = float(quantity)

        if choice == '1':
            print(f"Placing MARKET {side} order for {quantity} {symbol}...")
            order_manager.place_market_order(symbol, side, quantity)
        
        elif choice == '2':
            price = input("Enter price: ").strip()
            if not validate_price(price):
                print("Error: Invalid price. Must be a positive decimal.")
                continue
            
            price = float(price)
            print(f"Placing LIMIT {side} order for {quantity} {symbol} at {price}...")
            order_manager.place_limit_order(symbol, side, quantity, price)

if __name__ == "__main__":
    main()
