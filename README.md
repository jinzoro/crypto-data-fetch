# Cryptocurrency Trending Data Script

This script fetches and displays trending cryptocurrency data, including Bitcoin and Ethereum, from CoinGecko. Each coin's details are displayed in a unique color for easy readability.

## Features

- Retrieves trending cryptocurrency data from CoinGecko's API.
- Includes specific details like:
  - Current price
  - Market cap
  - Total volume
  - 24-hour price change
  - 7-day price change
  - Circulating supply
- Color-coded output to make each coin's data visually distinct.

## Requirements

- **Python 3.6+**
- **Dependencies**:
  - `requests`: For making HTTP requests to the CoinGecko API.
  - `colorama`: For color-coding the terminal output.

### Installation

Clone the repository if it is stored in a version control system, and navigate to the directory:
```
git clone <repository_url>
cd <repository_directory>
```

Install the required Python packages using `pip`:
```
pip install requests colorama
```

### Usage

Run the script using the following command:
```
python3 <script_name>.py
```

The script will fetch the current trending coins along with Bitcoin and Ethereum, and display relevant data, with each coin presented in a unique color.

### Code Overview

- **CoinGecko API**: The script uses the CoinGecko API to retrieve trending coin data and current market data for Bitcoin, Ethereum, and other trending coins.
- **Color Coding**: The script assigns each coin a unique color for better readability using the `colorama` library.
- **Rate Limiting**: A small delay (`time.sleep(2)`) is used between API requests to prevent rate limiting issues.

### Example Output

```
Trending Cryptocurrency Details:

Fetching data for bitcoin...
Name: Bitcoin (BTC)
Current Price: $30000
Market Cap: $600000000000
Total Volume: $25000000000
24-Hour Price Change: 2.5%
7-Day Price Change: -1.2%
Circulating Supply: 19000000

Fetching data for ethereum...
Name: Ethereum (ETH)
Current Price: $2000
Market Cap: $300000000000
Total Volume: $15000000000
24-Hour Price Change: -1.8%
7-Day Price Change: 3.1%
Circulating Supply: 110000000
```

### Notes

- **Error Handling**: The script checks for each coin's availability in CoinGecko’s `/coins/markets` endpoint, skipping any coin that doesn't return data.
- **Customization**: You can modify `coin_ids` to include other coins by adding their CoinGecko IDs.

### License

This project is licensed under the MIT License.
