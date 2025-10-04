"""
NSE Analysis - Stock data fetcher and analyzer for National Stock Exchange of India
"""

import requests
import pandas as pd
from typing import Optional, Dict, List
from datetime import datetime, timedelta


class NSEAnalyzer:
    """
    NSE Stock Data Analyzer
    
    This class provides methods to fetch and analyze stock data from NSE India.
    """
    
    def __init__(self):
        """Initialize NSE Analyzer with base URL and headers"""
        self.base_url = "https://www.nseindia.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_quote(self, symbol: str) -> Optional[Dict]:
        """
        Get real-time quote for a stock symbol
        
        Args:
            symbol: Stock symbol (e.g., 'RELIANCE', 'TCS')
            
        Returns:
            Dictionary containing stock quote data or None if failed
        """
        try:
            url = f"{self.base_url}/api/quote-equity?symbol={symbol}"
            # First request to get cookies
            self.session.get(self.base_url)
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Failed to fetch data for {symbol}. Status: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching quote for {symbol}: {str(e)}")
            return None
    
    def get_top_gainers(self) -> Optional[pd.DataFrame]:
        """
        Get top gaining stocks
        
        Returns:
            DataFrame with top gainers or None if failed
        """
        try:
            url = f"{self.base_url}/api/live-analysis-variations?index=gainers"
            self.session.get(self.base_url)
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    return pd.DataFrame(data['data'])
            return None
        except Exception as e:
            print(f"Error fetching top gainers: {str(e)}")
            return None
    
    def get_top_losers(self) -> Optional[pd.DataFrame]:
        """
        Get top losing stocks
        
        Returns:
            DataFrame with top losers or None if failed
        """
        try:
            url = f"{self.base_url}/api/live-analysis-variations?index=losers"
            self.session.get(self.base_url)
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'data' in data:
                    return pd.DataFrame(data['data'])
            return None
        except Exception as e:
            print(f"Error fetching top losers: {str(e)}")
            return None
    
    def calculate_simple_moving_average(self, prices: List[float], period: int) -> float:
        """
        Calculate Simple Moving Average
        
        Args:
            prices: List of stock prices
            period: Number of periods for SMA
            
        Returns:
            Simple moving average value
        """
        if len(prices) < period:
            raise ValueError(f"Not enough data points. Need {period}, got {len(prices)}")
        
        recent_prices = prices[-period:]
        return sum(recent_prices) / period
    
    def calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        """
        Calculate Relative Strength Index (RSI)
        
        Args:
            prices: List of stock prices
            period: RSI period (default: 14)
            
        Returns:
            RSI value
        """
        if len(prices) < period + 1:
            raise ValueError(f"Not enough data points. Need {period + 1}, got {len(prices)}")
        
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi


def main():
    """Example usage of NSE Analyzer"""
    analyzer = NSEAnalyzer()
    
    print("NSE Analysis Tool")
    print("=" * 50)
    
    # Example: Get quote for a symbol
    symbol = "RELIANCE"
    print(f"\nFetching quote for {symbol}...")
    quote = analyzer.get_quote(symbol)
    if quote:
        print(f"Quote data retrieved for {symbol}")
    
    # Example: Get top gainers
    print("\nFetching top gainers...")
    gainers = analyzer.get_top_gainers()
    if gainers is not None:
        print(f"Top gainers retrieved: {len(gainers)} stocks")
    
    # Example: Calculate SMA
    sample_prices = [100, 102, 101, 105, 107, 106, 108, 110, 109, 111]
    sma = analyzer.calculate_simple_moving_average(sample_prices, 5)
    print(f"\nSample SMA (5-period): {sma:.2f}")
    
    # Example: Calculate RSI
    rsi = analyzer.calculate_rsi(sample_prices, 5)
    print(f"Sample RSI (5-period): {rsi:.2f}")


if __name__ == "__main__":
    main()
