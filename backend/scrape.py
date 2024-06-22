from TikTokApi import TikTokApi
import asyncio
import os
import json

ms_token = "o9klnAWyT3w_bUO0rwZ_GM6CMaq1qGwZ_OL4iqC6Ajaa2EotpctFhZ_SkFa9G8gk85cuVceGsVGIYt6hKHrJm86aIZjcyMXqEg6UsOVzxwn5Kf-Scpdor0v3QbHOm4sNHjSPhWhy8wMN5MibKPkqqr0="# get your own ms_token from your cookies on tiktok.com
ms_token = os.getenv("MS_TOKEN", ms_token)
async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        async for video in api.trending.videos(count=1):
            print(video)
            print(video.as_dict)
            if __name__ == "__main__":
                with open('videos.json', 'w') as f:
                    json.dump(video.as_dict, f)

if __name__ == "__main__":
    asyncio.run(trending_videos())