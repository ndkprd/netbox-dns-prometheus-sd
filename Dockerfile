FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Nginx and other dependencies
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Nginx configuration file into the container
COPY nginx.conf /etc/nginx/nginx.conf

# Copy app and install dependencies.
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -e . 

# Create log dir.
RUN mkdir -p /var/log/netbox_dns_sd && \
    chmod -R 755 /var/log/netbox_dns_sd

# Symlink the output file to /usr/share/nginx/html
# RUN ln -s /app/output/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Set up entrypoint to start Nginx and the Python application
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
