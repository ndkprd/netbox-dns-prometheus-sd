import signal
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S%z",
    handlers=[
        logging.FileHandler("/var/log/netbox_dns_sd/message.log"),
        logging.StreamHandler()
    ]
)

def shutdown_handler(signal, frame):
    logging.info("Shutting down...")
    sys.exit(0)
