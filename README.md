# NSE Analysis

A Python-based tool for analyzing stocks listed on the National Stock Exchange (NSE) of India.

## Features

- **Real-time Stock Quotes**: Fetch current stock prices and information
- **Market Movers**: Get top gainers and losers in the market
- **Technical Indicators**: Calculate SMA (Simple Moving Average) and RSI (Relative Strength Index)
- **Easy-to-use API**: Simple and intuitive interface for stock analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prashantGit/nse_analysis.git
cd nse_analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from nse_analysis import NSEAnalyzer

# Initialize the analyzer
analyzer = NSEAnalyzer()

# Get stock quote
quote = analyzer.get_quote("RELIANCE")
if quote:
    print(f"Last Price: {quote['priceInfo']['lastPrice']}")

# Get top gainers
gainers = analyzer.get_top_gainers()
if gainers is not None:
    print(gainers.head())

# Get top losers
losers = analyzer.get_top_losers()
if losers is not None:
    print(losers.head())
```

### Technical Analysis

```python
from nse_analysis import NSEAnalyzer

analyzer = NSEAnalyzer()

# Sample price data
prices = [100, 102, 101, 105, 107, 106, 108, 110, 109, 111]

# Calculate Simple Moving Average
sma = analyzer.calculate_simple_moving_average(prices, period=5)
print(f"5-period SMA: {sma}")

# Calculate RSI
rsi = analyzer.calculate_rsi(prices, period=14)
print(f"RSI: {rsi}")
```

### Running Examples

Run the example script to see all features in action:

```bash
python example.py
```

## API Reference

### NSEAnalyzer Class

#### Methods

- `get_quote(symbol: str)` - Get real-time quote for a stock symbol
- `get_top_gainers()` - Get DataFrame of top gaining stocks
- `get_top_losers()` - Get DataFrame of top losing stocks
- `calculate_simple_moving_average(prices: List[float], period: int)` - Calculate SMA
- `calculate_rsi(prices: List[float], period: int)` - Calculate RSI

## Requirements

- Python 3.7+
- requests >= 2.31.0
- pandas >= 2.0.0
- numpy >= 1.24.0

## Limitations

- Data is fetched from NSE India website and depends on their API availability
- Rate limiting may apply based on NSE's policies
- Historical data fetching is not yet implemented

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and research purposes only. Always do your own research before making investment decisions.
