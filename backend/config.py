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
            hashtags = ["covid", 
                        "vaccine", 
                        "lockdown", 
                        "pandemic",
                        "donaltrump",
                        "joebiden",
                        "election",
                        "putin",
                        ]
        filter = [
            "fyp",
            "foryou",
            "viral",
            "comedy",
            "funny",
            "tiktok",
            "trending",
            "4u",
            "pov",
            "prank",
            "dance",
            "humor",
            "crazy",
        ]