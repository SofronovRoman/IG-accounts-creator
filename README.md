>### The script for educational purpose only, not for mass IG accounts creating 

<strong>Don't use free proxy servers or VPN because a high chance to get ban</strong>

## ⬇️ Installation
```ruby
$ git clone https://github.com/SofronovRoman/IG-accounts-creator.git
$ cd IG-accounts-creator
$ python3 -m pip install -r requirements.txt
```
## Configuration
Download [Chromedriver](https://chromedriver.chromium.org/downloads) for [Chrome](https://www.google.com/intl/en/chrome/)

Open config.py
| Config               | Usage                                                              |
| :------------------- | :----------------------------------------------------------------- |
| path_to_chromedriver | Path to Chromedriver                                               |
| proxy_server         | Settings for proxy server [ip address, port, username, password]   |

If you will use proxy server change setting 'proxy_server' in config.py and change main.py
```python
102       driver = settings_for_driver(use_proxy=True)
```
If you will use VPN dot'n change main.py

## Usage

```ruby
$ python3 main.py
```
All information about accounts (date of creation, username, email, password, cookies, user agent) are stored in accounts.db

You can add new names to 'utils\Names.txt' and new user agents to 'utils\user_agent.txt' for registration.
