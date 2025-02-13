# NETBOX DNS Prometheus SD

Turn your [Netbox](https://netboxlabs.com) DNS zones from [Netbox DNS](https://github.com/netbox-community/netbox-dns) plugin into a [Prometheus](https://prometheus.io/) HTTP service discovery. Format inspired by [netbox-plugin-prometheus-sd](https://github.com/FlxPeters/netbox-plugin-prometheus-sd.

*"Why not just make a plugin?"*

Sorry, I'm not smart enough yet for that.

## Usage

Every configuration needed is configurable from the environment variables.

| Environment Variable | Description | Example |
|----------------------|-------------|---------|
| NETBOX_API_URL | Netbox instance URL. | https://netbox.example.com |
| NETBOX_API_TOKEN | Netbox API token. | supersecrettoken69420 |
| NETBOX_DNS_VIEW_NAME | Netbox DNS view name for filtering. | "Default" |
| NETBOX_DNS_DATASOURCE_REFRESH_INTERVAL | Refresh interval in seconds. | 60 |

## License

[MIT](./LICENSE)
