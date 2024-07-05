import time
from TikTokApi import TikTokApi
from backend.config import Config
from collections import defaultdict
from transformers import pipeline

import asyncio
import math
import json


class Explorer:
    def __init__(self):
        self.ms_token = Config.Scraper.ms_token
        self.ydl_opts = Config.Scraper.ydl_opts
        self.suppress_resource_load_types = Config.Scraper.suppress_resource_load_types
        self.hashtags = defaultdict(int)
        self.hashtags_seeds = Config.Explorer.Seeds.hashtags
        self.filter = Config.Explorer.filter
    
    async def get_hashtags(self, depth = 5):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], 
                                            num_sessions=1, 
                                            sleep_after=1,
                                            headless=False,
                                            suppress_resource_load_types=self.suppress_resource_load_types,
                                            # browser='firefox'
                                            )
            current_depth = 0
            frontier = self.hashtags_seeds
            visited = set()
            while current_depth < depth:
                print(f"Searching at depth = {current_depth + 1} / {depth}")
                current_frontier = set()
                for old_tag in frontier: 
                    if old_tag in visited:
                        continue
                    print(f"Searching for #{old_tag}")
                    visited.add(old_tag)
                    tag = api.hashtag(name=old_tag)
                    tag_info = await tag.info()
                    tag_info = tag_info['challengeInfo']
                    view_count = int(tag_info['statsV2']['viewCount'])
                    video_count = int(tag_info['statsV2']['videoCount'])
                    tag_score = 0.8 ** current_depth + math.log10(view_count / (1e4*video_count)) * 0.1
                    number_video = math.ceil((math.log10(video_count) * 1.5 + math.log10(view_count)) * (0.6 ** current_depth))

                    ## BFS logic here ############################
                    count = 0
                    new_tags = set()
                    async for video in tag.videos(count=30):
                        count += 1
                        video_dict = video.as_dict
                        for new_tag_title in video_dict['challenges']:
                            new_tag = api.hashtag(name=new_tag_title['title'])
                            new_tag_info = await new_tag.info()
                            if any(f in new_tag_title['title'] for f in self.filter):
                                continue
                            if not new_tag.isalnum():
                                continue
                            if 'challengeInfo' not in new_tag_info or int(new_tag_info['challengeInfo']['statsV2']['videoCount']) < 1e5 or int(new_tag_info['challengeInfo']['statsV2']['viewCount']) < 1e11:
                                continue
                            # print(f"#{tag['title']}: {new_tag_info['challengeInfo']['statsV2']['videoCount']} videos, {new_tag_info['challengeInfo']['statsV2']['viewCount']} views")
                            new_tags.add(new_tag_title['title'])
                        if count >= number_video:
                            break
                    ## Update frontier and hashtags ################
                    self.hashtags[old_tag] = tag_score
                    current_frontier.update(new_tags)
                    print(new_tags)
                    with open('data/hashtags.json', 'w') as f:
                        json.dump(self.hashtags, f, indent=4)
                frontier = current_frontier
                current_depth += 1
        
    def process_filtered_tags(self):
        pass

if __name__ == "__main__":
    explorer = Explorer()
    asyncio.run(explorer.get_hashtags())