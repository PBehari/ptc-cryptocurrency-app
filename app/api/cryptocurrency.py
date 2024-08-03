
# Import modules
import requests

# Function to fetch data from the API
def get_api_data():
    """
    Fetch and yield data from the API.

    Yields:
    dict: A dictionary containing the cryptocurrency data.
    """

    url = 'https://api.coincap.io/v2/exchanges'

    # Send request
    response = requests.get(url=url)
    # Convert json string to a python dictionary
    response_json = response.json()

    if response_json and 'data' in response_json:
        # Loops trough the data and yield the response
        response_data = response_json.get('data', [])

        for data in response_data:
            # Extract relevant fields from each data entry
            yield {
                "name": data["name"],
                "percent_total_volume": data["percentTotalVolume"],
                "volume_usd": data["volumeUsd"],
                "trading_pairs": data["tradingPairs"],
                "exchange_url": data["exchangeUrl"],
                "updated": data["updated"],
            }
    else:
        # If the response data is empty or invalid, yield an empty dictionary
        yield {}

def sort_cryptocurrency(data, sort_column='name', reverse=False):
    """
    Sort data by name in ascending/descending order.

    Args:
        data (list): The data we want to sort

    Returns:
        list: The sorted data.
    """
    return sorted(data, key=lambda x: x[sort_column].lower(), reverse=reverse)

def filter_cryptocurrency(data, filter_by=None, filter_value=None):
    """
    Filter data based on a given filter.

    Args:
        data (list): The data on which we want to apply the filter.
        filter_by (str): The field on which to filter.
        filter_value (str): The value to filter on.

    Returns:
        list: The filtered data
    """
    if filter_by == 'month':
        # Filter by month (MM)
        return filter(lambda x: x['date'][5:7] == filter_value.zfill(2), data)
    elif filter_by == 'name':
        # Filter by name (case-insensitive)
        return filter(lambda x: filter_value.lower() in x['name'].lower(), data)
    else:
        # Return the original data if no filter is applied
        return data