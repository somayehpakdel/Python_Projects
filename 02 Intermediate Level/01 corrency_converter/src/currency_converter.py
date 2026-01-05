import datetime
import logging
from typing import Tuple

import humanize
import requests
from cachetools import TTLCache, cached

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


cache: TTLCache = TTLCache(maxsize=1000, ttl=3600)  # Cache for 1 hour


@cached(cache)
def get_exchange_rate(base_currency: str, target_currency: str) -> Tuple[float, int]:
    """Fetch the exchange rate between two currencies.

    This function retrieves the current exchange rate from an external API 
    and caches the result for one hour to improve performance.

    Args:
        base_currency: The currency to convert from (e.g., 'USD').
        target_currency: The currency to convert to (e.g., 'EUR').

    Returns:
        tuple: A tuple containing:
            - exchange_rate: The exchange rate from base_currency to target_currency.
            - time_last_updated: The timestamp of when the exchange rate was last updated.
    
    Raises:
        KeyError: If the target_currency is not found in the API response.
        requests.exceptions.RequestException: For network-related errors while fetching data.
    """

    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)

    try:
        response.raise_for_status() # Raise an error for bad responses (4xx and 5xx)
        data = response.json()
        if target_currency not in data["rates"]:
            raise ValueError(f"Currency '{target_currency}' not found in the API response.")
        exchange_rate = data["rates"][target_currency] 
        time_last_updated = data["time_last_updated"]
        return exchange_rate, time_last_updated

    except requests.exceptions.HTTPError as e:
        logger.error(f'Network error occurred: {e}')
        raise 
    except ValueError as e:
        logger.error(f'Currency {target_currency} not found in the API response.')
        raise 
    except Exception as e:
        logger.error(f'Unexpected error occurred: {e}')
        raise 

def convert_currency(amount: float, exchange_rate: float) -> float:
    """Convert an amount from one currency to another using the given exchange rate.

    Args:
        amount: The amount of money to be converted.
        exchange_rate: The conversion rate to apply.

    Returns:
        float: The converted amount in the target currency.
    """
    converted_amount = amount * exchange_rate
    return converted_amount


def humanize_time(time_last_updated: int) -> str:
    """
    Convert a timestamp into a human-readable time difference.

    Args:
        time_last_updated: The timestamp of when the exchange rate was last updated.

    Returns:
        str: A human-readable string representing the time since the last update.
    """
    diff_time = datetime.datetime.now() - datetime.datetime.fromtimestamp(time_last_updated)
    return humanize.naturaltime(diff_time)


if __name__ == '__main__':

    base_currency = input("Enter the base currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    amount = float(input("Enter the amount to convert: "))

    exchange_rate, time_last_updated = get_exchange_rate(base_currency, target_currency)
    converted_amount = convert_currency(amount, exchange_rate)

    time_last_updated_humanize: str = humanize_time(time_last_updated)

    print(f"{amount} {base_currency} is equal to {converted_amount:.4f} {target_currency}")
    print(f"Exchange rate as of {time_last_updated_humanize}")
    