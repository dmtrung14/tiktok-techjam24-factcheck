import collections
import json
from TikTokApi import TikTokApi
import asyncio
import os
import math

ms_token = os.environ.get("ms_token", None)  # set your own ms_token
hashtags = collections.defaultdict(int)

def test():
    pass
