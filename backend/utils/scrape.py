import math
from TikTokApi import TikTokApi
from yt_dlp import YoutubeDL
from backend.config import Config
from collections import defaultdict
import asyncio
import json


class TikTokScraper:
    def __init__(self):
        self.api = TikTokApi()
        self.ms_token = Config.Scraper.ms_token
        self.ydl_opts = Config.Scraper.ydl_opts
        self.suppress_resource_load_types = Config.Scraper.suppress_resource_load_types
        self.hashtags = Config.Scraper.hashtags
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

    async def get_video_by_hashtag(self):

        async with TikTokApi() as api:
            await api.create_sessions(ms_tokens=[self.ms_token], 
                                      num_sessions=1, 
                                      sleep_after=3, 
                                      headless=False,
                                      suppress_resource_load_types=self.suppress_resource_load_types)
            scraped_videos = dict()
            tag_to_video = defaultdict(list)
            total_videos = 0
            for hashtag in self.hashtags:
                tag = api.hashtag(name=hashtag)
                number_video = math.ceil(max(1, 100 * (self.hashtags[hashtag] ** 1.5)))
                total_videos += number_video
                count = 0
                print(f"Scraping {number_video} videos for #{hashtag}")
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
                    count += 1
                    scraped_videos[video_info['id']] = save_info
                    tag_to_video[hashtag].append(video_info['id'])
                    if count >= number_video:
                        break
                with open('data/videos.json', 'w') as f:
                    json.dump(scraped_videos, f, indent=4)
            print("Successfully scraped", total_videos, "videos for top", len(self.hashtags), "hashtags.")


    async def close(self):
        await self.api.close()
    

if __name__ == "__main__":
    scraper = TikTokScraper()
    asyncio.run(scraper.get_video_by_hashtag())