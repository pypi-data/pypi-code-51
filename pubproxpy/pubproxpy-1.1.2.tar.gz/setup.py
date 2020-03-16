# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pubproxpy']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'pubproxpy',
    'version': '1.1.2',
    'description': 'An easy to use Python wrapper for pubproxy.com',
    'long_description': '# Pubproxpy\n\nAn easy to use Python wrapper for [pubproxy](http://pubproxy.com)\'s public proxy API.\n\n## Installation\n\n**NOTE:** The minimum python version for this library is 3.7, check with `python -V` or `python3 -V` if you\'re unsure about your current version.\n\nInstall the [pubproxpy](https://pypi.org/project/pubproxpy/) package using your standard Python package manager e.g.\n\n```bash\n$ pip install pubproxpy\n```\n\nAs always you are recommended to install into a virtual environment.\n\n## Keyless API Limitations\n\n### API Daily Limits\n\nAt the time of writing this without an API key the pubproxy API limits users to 5 proxies per request and 50 requests per day. The maximum proxies per request is always used to minimize rate limiting along with getting the most proxies possible within the request limit meaning you should get 250 proxies per day without needing an API key.\n\n### API Rate Limiting\n\nWithout an API key pubproxy limits users to one request per second so a `ProxyFetcher` will try to ensure that at most only one request per second is done without an API key. This is synchronized between `ProxyFetcher`s, but this is not thread safe so make sure all `ProxyFetcher`s are on one thread in one program if you have no API key. The rate limiting is quite severe, so upon being hit the API seems to deny requests for several minutes/hours.\n\n## Quickstart Example\n\n```python\nfrom pubproxpy import ProxyFetcher\n\n# ProxyFetcher for proxies that use the socks5 protocol, are located in\n# the US or Canada and support POST requests\nsocks_pf = ProxyFetcher(protocol="socks5", countries=["US", "CA"], post=True)\n\n# ProxyFetcher for proxies that support https, are elite anonymity level,\n# and connected in 15 seconds or less\nhttps_pf = ProxyFetcher(\n    protocol="http", https=True, level="elite", time_to_connect=15\n)\n\n# Get one socks proxy, followed by 10 https proxies\n# NOTE: even though there are multiple `ProxyFetcher`s the delays are\n#       coordinated between them to prevent rate limiting\nsocks_proxy = socks_pf.get_proxy()      # Returns a single proxy as a string\nhttps_proxy = https_pf.get_proxies(10)  # Returns a list of proxies as strings\n\n# Do something with the proxies, like spawn worker threads that use them\n```\n\n## Documentation\n\nGetting proxies is handled by the `ProxyFetcher` class. There are several parameters you can pass on initialization to narrow down the proxies to a suitable type. From there you can just call `get_proxy` to receive a proxy in the form of `{ip-address}:{port-number}` or call `get_proxies(amount)` to receive a list of `amount` proxies. There is an internal blacklist to ensure that the same proxy ip and port combo will not be used more than once by any `ProxyFetcher`, unless `exclude_used` is `False`.\n\n### `ProxyFetcher` Parameters\n\nSince the API doesn\'t check pretty much anything for correctness, we do our best in the `ProxyFetcher` to ensure nothing is wrong. As far as I know the only thing that isn\'t checked is that the `countries` or `not_countries` actually use the correct codes.\n\n|Parameter|Type|Description|\n|:--|:--|:--|\n|`exclude_used`|`bool` |[_Default: `True`_] If the `ProxyFetcher` should prevent re-returning proxies|\n|`api_key`|`str`|API key for a paid account, you can also set `$PUBPROXY_API_KEY` to pass your key, passing the `api_key` parameter will override the env-var if both are present|\n|`level`|`str`|[_Options: `"anonymous"`, `"elite"`_] Proxy anonymity level|\n|`protocol`|`str`|[_Options: "`"http`, `"socks4"`, `"socks5"`_] Desired communication protocol|\n|`countries`|`str` or `list<str>`|Locations of the proxy using the [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, **Incompatible with `not_countries`**|\n|`not_countries`|`str` or `list<str>`|Blacklist locations of the proxy using the [ISO-3166 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, **Incompatible with `countries`**|\n|`last_checked`|`int`|[_Bounds: 1-1000_] Minutes since the proxy was checked|\n|`port`|`int`|Proxies using a specific port|\n|`time_to_connect`|`int`|[_Bounds: 1-60_] How many seconds it took for the proxy to connect|\n|`cookies`|`bool`|Supports requests with cookies|\n|`google`|`bool`|Can connect to Google|\n|`https`|`bool`|Supports HTTPS requests|\n|`post`|`bool`|Supports POST requests|\n|`referer`|`bool`|Supports referer requests|\n|`user_agent`|`bool`|Supports forwarding user-agents|\n\n### `ProxyFetcher` Methods\n\nKeeping it simple (stupid), so just `get_proxy()`, `get_proxies(amount)`, and `drain()`.\n\n|Method|Returns|\n|:--|:--|\n|`get_proxy()`|Single proxy as a string, format `{ip}:{port}`|\n|`get_proxies(amount)`|List of `amount` proxies, same format as above|\n|`drain()`|Returns any proxies remaining in the current list, useful if you are no longer getting proxies and want to save any left over|\n\n### Exceptions\n\nAll the exceptions are defined in `pubproxy.errors`.\n\n|Exception|Description|\n|:--|:--|\n|`ProxyError`|Base exception that all other pubproxpy errors inherit from, also raised when the API returns an unknown response|\n|`APIKeyError`|Error raised when the API gives an incorrect API Key response|\n|`RateLimitError`|Error raised when the API gives a rate-limiting response (more than 1 request per second)|\n|`DailyLimitError`|Error raised when the API gives the daily request limit response|\n\n',
    'author': 'LovecraftianHorror',
    'author_email': 'LovecraftianHorror@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/LovecraftianHorror/pubproxpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
