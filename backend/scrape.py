import math
from TikTokApi import TikTokApi
from yt_dlp import YoutubeDL
from config import Config
import asyncio
import json


class TikTokScraper:
    def __init__(self):
        self.api = TikTokApi()
        self.ms_token = Config.Scraper.ms_token
        self.ydl_opts = Config.Scraper.ydl_opts
        self.suppress_resource_load_types = Config.Scraper.suppress_resource_load_types

    def remove_tags(self, video):
        text = video['desc']
        for tag in video['challenges']:
            text = text.replace(f'#{tag["title"]}', '')
        return text


    async def trending_videos(self):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], 
                                      num_sessions=1, 
                                      sleep_after=3, 
                                      headless=False,
                                      suppress_resource_load_types=self.suppress_resource_load_types)
            async for video in api.trending.videos(count=1):
                with open('data/videos.json', 'w') as f:
                    json.dump(video.as_dict, f, indent=4)

    async def get_video_by_hashtag(self, hashtags: list[str]):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], 
                                      num_sessions=1, 
                                      sleep_after=3, 
                                      headless=False,
                                      suppress_resource_load_types=self.suppress_resource_load_types)
            for hashtag in hashtags:
                tag = api.hashtag(name=hashtag)
                number_video = max(1, 20 - math.log(hashtags[hashtag], 0.8) * 3)
                async for video in tag.videos(count = 1):
                    video_info = video.as_dict
                    save_info = dict()
                    save_info['author'] = {
                        'uniqueId': video_info['author']['uniqueId'],
                        'signature': video_info['author']['signature'],
                    }
                    save_info['challenges'] = [challenge['title'] for challenge in video_info['challenges']]
                    save_info['desc'] = self.remove_tags(video_info)
                    save_info['isAd'] = video_info['isAd']
                    save_info['music'] = video_info['music']['playUrl']
                    

                    with open(f'data/{hashtag}_videos.json', 'w') as f:
                        json.dump(video.as_dict, f, indent=4)

    async def close(self):
        await self.api.close()
    

if __name__ == "__main__":
    scraper = TikTokScraper()
    asyncio.run(scraper.get_hashtag_videos())