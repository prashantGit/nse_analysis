"""
Example script demonstrating NSE Analysis capabilities
"""

from nse_analysis import NSEAnalyzer


def example_stock_quote():
    """Example: Fetch stock quote"""
    print("\n" + "="*60)
    print("Example 1: Fetching Stock Quote")
    print("="*60)
    
    analyzer = NSEAnalyzer()
    symbols = ["RELIANCE", "TCS", "INFY"]
    
    for symbol in symbols:
        print(f"\nFetching quote for {symbol}...")
        quote = analyzer.get_quote(symbol)
        if quote and 'priceInfo' in quote:
            price_info = quote['priceInfo']
            print(f"  Last Price: {price_info.get('lastPrice', 'N/A')}")
            print(f"  Change: {price_info.get('change', 'N/A')}")
            print(f"  % Change: {price_info.get('pChange', 'N/A')}")


def example_market_movers():
    """Example: Fetch top gainers and losers"""
    print("\n" + "="*60)
    print("Example 2: Market Movers (Top Gainers & Losers)")
    print("="*60)
    
    analyzer = NSEAnalyzer()
    
    print("\nTop Gainers:")
    gainers = analyzer.get_top_gainers()
    if gainers is not None and not gainers.empty:
        print(gainers.head(5))
    else:
        print("  Unable to fetch gainers data")
    
    print("\nTop Losers:")
    losers = analyzer.get_top_losers()
    if losers is not None and not losers.empty:
        print(losers.head(5))
    else:
        print("  Unable to fetch losers data")


def example_technical_indicators():
    """Example: Calculate technical indicators"""
    print("\n" + "="*60)
    print("Example 3: Technical Indicators")
    print("="*60)
    
    analyzer = NSEAnalyzer()
    
    # Sample price data (in real scenario, this would come from historical data)
    prices = [100, 102, 101, 105, 107, 106, 108, 110, 109, 111, 113, 112, 115, 117, 116]
    
    print(f"\nSample prices: {prices}")
    
    # Calculate SMA for different periods
    for period in [5, 10]:
        try:
            sma = analyzer.calculate_simple_moving_average(prices, period)
            print(f"SMA ({period}-period): {sma:.2f}")
        except ValueError as e:
            print(f"SMA ({period}-period): {e}")
    
    # Calculate RSI
    try:
        rsi = analyzer.calculate_rsi(prices, 14)
        print(f"RSI (14-period): {rsi:.2f}")
        
        if rsi > 70:
            print("  → Overbought condition")
        elif rsi < 30:
            print("  → Oversold condition")
        else:
            print("  → Neutral")
    except ValueError as e:
        print(f"RSI: {e}")


def main():
    """Run all examples"""
    print("\n" + "#"*60)
    print("# NSE Analysis - Example Usage")
    print("#"*60)
    
    # Run examples
    example_technical_indicators()
    
    # Note: The following examples require internet connection to NSE
    print("\n\nNote: The following examples require internet connection to NSE India")
    print("They may fail if NSE website is down or blocks the requests.")
    
    try:
        example_stock_quote()
    except Exception as e:
        print(f"Stock quote example failed: {e}")
    
    try:
        example_market_movers()
    except Exception as e:
        print(f"Market movers example failed: {e}")
    
    print("\n" + "#"*60)
    print("# Examples completed")
    print("#"*60 + "\n")


if __name__ == "__main__":
    main()
