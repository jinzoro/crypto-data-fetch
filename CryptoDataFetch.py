import requests
from colorama import Fore, Style, init
from itertools import cycle
import time

# Initialize colorama for Windows compatibility
init(autoreset=True)

# List of colors to apply to each coin (cycling through)
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
color_cycle = cycle(colors)  # Cycle through colors

# CoinGecko URLs
trending_url = "https://api.coingecko.com/api/v3/search/trending"
market_url = "https://api.coingecko.com/api/v3/coins/markets"

# Prepare the list of coins to track
coin_ids = ["bitcoin", "ethereum"]

# Fetch trending coin data from CoinGecko and add to the list
response = requests.get(trending_url)
trending_data = response.json()
coin_ids.extend([item['item']['id'] for item in trending_data['coins']])

# Display detailed information for each coin
print("Trending Cryptocurrency Details:")
for coin_id in coin_ids:
    print(f"\nFetching data for {coin_id}...")

    # Get current market data for each coin
    params = {
        "vs_currency": "usd",
        "ids": coin_id
    }
    market_response = requests.get(market_url, params=params)
    time.sleep(2)  # Add a small delay to avoid API rate limiting

    # Check if the response is valid and contains data
    if market_response.status_code == 200 and market_response.content:
        market_data = market_response.json()
    else:
        print(f"Warning: Could not fetch data for {coin_id}. Skipping...")
        continue

    # Process and display market data if available
    if market_data:
        coin_data = market_data[0]
        name = coin_data['name']
        symbol = coin_data['symbol'].upper()
        current_price = coin_data['current_price']
        market_cap = coin_data['market_cap']
        volume = coin_data['total_volume']
        price_change_24h = coin_data.get('price_change_percentage_24h', 'N/A')
        price_change_7d = coin_data.get('price_change_percentage_7d_in_currency', 'N/A')
        circulating_supply = coin_data.get('circulating_supply', 'N/A')

        # Assign a unique color to each coin by cycling through the color list
        color = next(color_cycle)

        # Display details with color
        print(color + f"Name: {name} ({symbol})")
        print(color + f"Current Price: ${current_price}")
        print(color + f"Market Cap: ${market_cap}")
        print(color + f"Total Volume: ${volume}")
        print(color + f"24-Hour Price Change: {price_change_24h}%")
        print(color + f"7-Day Price Change: {price_change_7d}%")
        print(color + f"Circulating Supply: {circulating_supply}")
    else:
        print(f"Warning: No market data available for {coin_id}.")
