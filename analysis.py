import pandas as pd
from datetime import datetime, timedelta

def calculate_moving_averages(breeze, stock_code, exchange_code='NSE', product_type='cash'):
    """
    Calculates the 10, 20, 50, 100, and 200-day moving averages for a given stock.

    :param breeze: An authenticated BreezeConnect instance.
    :param stock_code: The stock code for which to calculate the moving averages.
    :param exchange_code: The exchange code (default is 'NSE').
    :param product_type: The product type (default is 'cash').
    :return: A dictionary containing the calculated moving averages.
    """
    to_date = datetime.now()
    from_date = to_date - timedelta(days=400)  # Fetch more data to ensure enough for 200 DMA

    try:
        historical_data = breeze.get_historical_data_v2(
            interval="1day",
            from_date=from_date.strftime('%Y-%m-%dT07:00:00.000Z'),
            to_date=to_date.strftime('%Y-%m-%dT07:00:00.000Z'),
            stock_code=stock_code,
            exchange_code=exchange_code,
            product_type=product_type
        )

        if historical_data['Success']:
            df = pd.DataFrame(historical_data['Success'])
            df['close'] = pd.to_numeric(df['close'])

            moving_averages = {
                '10_dma': df['close'].rolling(window=10).mean().iloc[-1],
                '20_dma': df['close'].rolling(window=20).mean().iloc[-1],
                '50_dma': df['close'].rolling(window=50).mean().iloc[-1],
                '100_dma': df['close'].rolling(window=100).mean().iloc[-1],
                '200_dma': df['close'].rolling(window=200).mean().iloc[-1],
            }
            return moving_averages
        else:
            return None
    except Exception as e:
        print(f"Error fetching historical data for {stock_code}: {e}")
        return None