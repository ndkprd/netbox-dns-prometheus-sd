import os
import signal
import time
import logging
from netbox_dns_sd.fetch import fetch_netbox_dns_data
from netbox_dns_sd.template import template_datasource
from utils.file_handler import export_to_html
from utils.exit import shutdown_handler

interval = int(os.getenv("NETBOX_DNS_DATASOURCE_REFRESH_INTERVAL", 300))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    handlers=[
        logging.FileHandler("/var/log/netbox_dns_datasource/message.log"),
        logging.StreamHandler()
    ]
)

def main():
    signal.signal(signal.SIGINT, shutdown_handler)
    signal.signal(signal.SIGTERM, shutdown_handler)
    while True:
        try:
            try:
                logging.info("Fetching DNS data from Netbox...")
                data = fetch_netbox_dns_data()
                
                logging.info("Rendering template...")
                templated_data = template_datasource(data)
                
                logging.info("Exporting to HTML...")
                export_to_html(templated_data)
                
                logging.info("Datasource updated successfully.")

            except Exception as e:
                logging.error(f"Failed to update datasource with error: {e}")
            
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(interval)
    
    # pretty_data = json.dumps(data, indent=4)
    # print(pretty_data)

if __name__ == "__main__":
    main()
