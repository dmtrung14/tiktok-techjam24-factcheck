import os


class Config:
    class Scraper:
        ms_token = os.getenv("MS_TOKEN", "o9klnAWyT3w_bUO0rwZ_GM6CMaq1qGwZ_OL4iqC6Ajaa2EotpctFhZ_SkFa9G8gk85cuVceGsVGIYt6hKHrJm86aIZjcyMXqEg6UsOVzxwn5Kf-Scpdor0v3QbHOm4sNHjSPhWhy8wMN5MibKPkqqr0=")
        ydl_opts = {
            'outtmpl': '%(uploader)s_%(id)s.%(ext)s',
        }
        suppress_resource_load_types = ["image", "media", "font", "stylesheet"]
        
    class Explorer:
        class Seeds:
            hashtags = ["covid",  "vaccine", "lockdown", "pandemic",
                        "donaltrump","joebiden","election","putin",
                        ]
        filter = [
            "fyp", "foryou", "viral", "comedy", "tiktok",
            "trending", "4u", "pov", "prank", "dance", "humor",
            "crazy", 'longervideos', 'minecraft', 'fy', 'parati', 'xyz',
            'abc', 'xzy', 'zyx', 'zxy', 'yxz', 'yzx', 'makemefamous', 'trend', 'meme', 'xh',
            'longervideos', 'relatable', 'sad', 'fun', 'real', 'capcut',
            'music', 'amazing', 'duet', 'yummy','asmr', 'mukbang',
            'fail','skit','omg','joke','wow','cute','sad','drawing',
            'fürdich','рекомендации','pourtoi','gaming',
            'movie', 'bestfriend', 'bff', 'foru', 'forupage',
            'slowmo', 'perte', 'explore', 'tutorial', 'edit', 
            'lifehack', 'girl', 'boy', 'gta', 'respect', 'neiperte',
            'LiveForTheChallenge', 'animation', 'cat', 'dog',
            'fortnite', 'greenscreen', 'rec', 'komedi', 'komedia',
            'like', 'follow', 'followme', 'followforfollow', 'comedi', 'hot',
            'cosplay', 'lmao', 'lol', 'blowthisup', 'blowup','share', 
            'viralvideo', 'cleantok', "ad", "sponsored", "promotion",
            "promoted", "tiktokpartner", "partner", "tiktokad",
        ]
    
    class Dataset:
        class BertMNLIYahoo:
            model = 'joeddav/bart-large-mnli-yahoo-answers'
            task = 'zero-shot-classification'
            labels = [
                'covid', 'vaccine',
                'donald trump', 'joe biden', 'us election',
                'america', 'putin', 'russia', 'us vs russia',
                'ukraine', 'lgbt'
            ]

    class Train:
        pass
        
