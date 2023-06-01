import random
import time
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Read config.ini file
config_file = "config.ini"
parser = ConfigParser()
parser.read(config_file, encoding='utf-8')

# Get configuration values
min_time = int(parser.get("Settings", "min_time"))
max_time = int(parser.get("Settings", "max_time"))

# Load proxy list from socks5_proxies.txt
proxy_list_file = "socks5_proxies.txt"
with open(proxy_list_file, "r") as file:
    proxy_list = [line.strip() for line in file]

# Load video links from link.txt
link_file = "link.txt"
with open(link_file, "r") as file:
    video_links = [line.strip() for line in file]

# Iterate through proxies and visit video links
for proxy in proxy_list:
    # Set up proxy for Selenium
    proxy_object = Proxy()
    proxy_object.proxy_type = ProxyType.MANUAL
    proxy_object.http_proxy = proxy
    proxy_object.ssl_proxy = proxy

    # Configure Chrome options with proxy
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--proxy-server={}".format(proxy))

    # Create Chrome driver with proxy
    driver = webdriver.Chrome(options=chrome_options)

    for link in video_links:
        # Visit the video link
        driver.get(link)

        # Generate random watching time between min_time and max_time
        watching_time = random.randint(min_time, max_time)
        print("Watching {} for {} seconds using proxy {}".format(link, watching_time, proxy))

        # Wait for the watching time
        time.sleep(watching_time)

    driver.quit()
