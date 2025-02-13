import os
import requests
# import json
import logging

def fetch_netbox_dns_data():
    """
    Fetch the DNS zones data from the NetBox API.

    The function fetches the DNS zones data from the NetBox API and
    returns it as a JSON object. The function requires two environment
    variables: NETBOX_API_URL and NETBOX_API_TOKEN to be set. The
    function will return a JSON object containing the DNS zone names
    and their corresponding IDs.

    :return: The JSON object containing the DNS zones data
    :rtype: dict
    """

    netbox_api_url = os.getenv("NETBOX_API_URL")
    netbox_api_token = os.getenv("NETBOX_API_TOKEN")
    netbox_api_headers = {
        "Authorization": f"Token {netbox_api_token}",
    }
    
    netbox_dns_view_name = os.getenv("NETBOX_DNS_VIEW_NAME")
    netbox_api_dns_url = f"{netbox_api_url}/api/plugins/netbox-dns/zones?format=json&view={netbox_dns_view_name}"
    
    response = requests.get(netbox_api_dns_url, headers=netbox_api_headers)
    response.raise_for_status()
    return response.json()
