# NETBOX DNS Prometheus SD

Turn your [Netbox](https://netboxlabs.com) DNS zones from [Netbox DNS](https://github.com/netbox-community/netbox-dns) plugin into a [Prometheus](https://prometheus.io/) HTTP service discovery. Format inspired by [netbox-plugin-prometheus-sd](https://github.com/FlxPeters/netbox-plugin-prometheus-sd.

*"Why not just make a plugin?"*

~~decoupling~~
~~domain-driven design~~
~~sidecar setup~~

Yeah, sorry, I'm not smart enough yet for that. But I do feel like this setup is more easier to manage. If you want to achieve a "plugin-like" feel, you can also just put the html page under your Netbox subpath, since it's only one single HTML page anyway. If you're using Docker/Kubernetes setup, you can also just run this as a sidecar container on the same deployment/host.

## Usage

Every configuration needed is configurable from the environment variables.

| Environment Variable | Description | Example |
|----------------------|-------------|---------|
| NETBOX_API_URL | Netbox instance URL. | https://netbox.example.com |
| NETBOX_API_TOKEN | Netbox API token. | supersecrettoken69420 |
| NETBOX_DNS_VIEW_NAME | Netbox DNS view name for filtering. | "Default" |
| NETBOX_DNS_SD_REFRESH_INTERVAL | Refresh interval in seconds. | 60 |
| NETBOX_DNS_SD_FILE_PATH | Path to the output file. | `./output` |

After it started running, it will query the DNS plugin API endpoint periodically, and the generate an HTML file inside of the directory you set in `NETBOX_DNS_SD_FILE_PATH` variable.

>**Note:**:
>
>If you're using container setup, you shouldn't need to set the `NETBOX_DNS_SD_FILE_PATH` variable. It will be created inside where the container needed.

## License

[MIT](./LICENSE)
