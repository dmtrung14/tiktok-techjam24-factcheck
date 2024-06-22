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

    async def get_hashtag_videos(self):
        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], 
                                      num_sessions=1, 
                                      sleep_after=3, 
                                      headless=False,
                                      suppress_resource_load_types=self.suppress_resource_load_types)
            tag = api.hashtag(name="covid")
            count = 0
            async for video in tag.videos(count=1):
                count += 1
                video_url = f"https://www.tiktok.com/@{video.author.username}/video/{video.id}"
                with open('data/hashtag_covid.json', 'w') as f:
                    json.dump(video.as_dict, f, indent=4)
                with YoutubeDL(self.ydl_opts) as ydl:
                    ydl.download([video_url])
                if count >= 1:
                    break
    async def close(self):
        await self.api.close()
    

if __name__ == "__main__":
    scraper = TikTokScraper()
    asyncio.run(scraper.get_hashtag_videos())