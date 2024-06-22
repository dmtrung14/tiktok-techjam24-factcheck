import pyktok as pyk 
videos = ['https://www.tiktok.com/@tiktok/video/7106594312292453675?is_copy_url=1&is_from_webapp=v1']
pyk.save_tiktok(videos, True, 'video_data.csv', 'chrome')