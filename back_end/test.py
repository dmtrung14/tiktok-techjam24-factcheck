import collections
import json
from TikTokApi import TikTokApi
import asyncio
import os
import math

ms_token = os.environ.get("ms_token", None)  # set your own ms_token
hashtags = collections.defaultdict(int)

async def get_hashtag_videos():
    async with TikTokApi() as api:
        print(ms_token)
        await api.create_sessions(ms_tokens=[ms_token], 
                                  num_sessions=1, 
                                  sleep_after=3,
                                  headless=False,
                                #   browser='firefox'
                                  )
        count = 0
        tag = api.hashtag(name="funny")
        tag_info = await tag.info()
        async for video in tag.videos(count=1):
            print(video)
        # print(tag_info)

async def expand_frontier(tag_name: str, number_video: int):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], 
                                    num_sessions=1, 
                                    sleep_after=3, 
                                    headless=False,
                                    # browser='firefox'
        )
        tag = api.hashtag(name=tag_name)
        count = 0
        new_tags = set()
        async for video in tag.videos(count=30):
            count += 1
            video_dict = video.as_dict
            for tag in video_dict['challenges']:
                new_tags.add(tag['title'])
            if count >= number_video:
                break
    return list(new_tags)


async def get_hashtags(depth = 5):
        
        current_depth = 0
        frontier = ["trump", "biden"]
        visited = set()
        while current_depth < depth:
                print(f"Searching at depth = {current_depth + 1} / {depth}")
                current_frontier = set()
                for old_tag in frontier:
                    async with TikTokApi() as api:
                        await api.create_sessions(ms_tokens=[ms_token], 
                                                num_sessions=1, 
                                                sleep_after=3,
                                                headless=False,
                                                #   suppress_resource_load_types=self.suppress_resource_load_types,
                                                browser='firefox'
                                                )
                        if old_tag in visited:
                            continue
                        print(f"Searching for #{old_tag}")
                        visited.add(old_tag)
                        tag = api.hashtag(name=old_tag)
                        tag_info = await tag.info()
                        number_video = 1
                        new_tags = await expand_frontier(tag_name = old_tag,
                                                            number_video = number_video)
                        current_frontier.update(new_tags)
                        print(new_tags)
                frontier = current_frontier
                current_depth += 1
        with open('data/hashtags.json', 'w') as f:
            json.dump(hashtags, f, indent=4)
if __name__ == "__main__":
    # asyncio.run(get_hashtag_videos())
    # asyncio.run(expand_frontier("funny", 30))
    asyncio.run(get_hashtags())