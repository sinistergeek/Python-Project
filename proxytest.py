import logging
from json.decoder import JSONDecodeError
from pathlib import Path
import pandas as pd
import requests
from requests.exceptions import ProxyError

logging.basicConfig(level=logging.INFO)
