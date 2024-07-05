import os
import json


class Config:
    class Scraper:
        ms_token = os.getenv("MS_TOKEN", "o9klnAWyT3w_bUO0rwZ_GM6CMaq1qGwZ_OL4iqC6Ajaa2EotpctFhZ_SkFa9G8gk85cuVceGsVGIYt6hKHrJm86aIZjcyMXqEg6UsOVzxwn5Kf-Scpdor0v3QbHOm4sNHjSPhWhy8wMN5MibKPkqqr0=")
        ydl_opts = {
            'outtmpl': '%(uploader)s_%(id)s.%(ext)s',
        }
        suppress_resource_load_types = ["image", "media", "font", "stylesheet"]
        with open('data/hashtags.json') as file:
            hashtags = json.load(file)
            hashtags_sorted = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
            min_score = hashtags_sorted[50][1]
            max_score = hashtags_sorted[0][1]
            diff = max_score - min_score
            hashtags = dict()
            for key, value in hashtags_sorted[:50]:
                hashtags[key] = (value - min_score) / diff * 0.85 + 0.15


    class Explorer:
        class Seeds:
            hashtags = ["covid",  "vaccine", "lockdown", "pandemic",
                        "donaldtrump","joebiden","election","putin",
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
            "mom", "outfit", "fnaf", 'charlidamelio', 'charli', 'dixie',
            'wwe', 'stitch', 'creepy', '1m', '100k', 'rip', 'crush', 'pubg',
            'phimhay', 'scary', 'cartoon', 'horror', 'kdrama', 'series',
            'tips', "couple", "relationship", "love", "romance", "kiss",
        ]
    
    class Dataset:
        class BertMNLIYahoo:
            model = 'joeddav/bart-large-mnli-yahoo-answers'
            task = 'zero-shot-classification'
            labels = [
                'covid', 'vaccine',
                'donald trump', 'joe biden', 'us election',
                'america', 'putin', 'russia', 'us vs russia',
                'ukraine', 'lgbt', 'euro', 'copa america',
            ]
            topics = [
                'politics', 'president', 'public health', 
                'economics','sports', 'science', 'technology',
                'human rights', 
            ]
            sentiments = ['positive', 'negative', 'neutral']

            with open('data/videos.json') as file:
                videos = json.load(file)
            with open('data/reduced_hashtags.json') as file:
                hashtags = json.load(file)

    class Train:
        aggregate_data = False # just load currently available data
        epochs = 10
        batch_size = 8
        learning_rate = 1e-5
        max_length = 512
        model = 'joeddav/bart-large-mnli-yahoo-answers'

    class Model:
        usr_msg1 = """You are given a user utterance that contain content of a short video.
Your task is to create a multiple choice quiz based on that content.
Question: [the question it self]\nA)Option A\nB)Option B\nC)Option C\nD)Option D\nAnswer: [the correct answer]\n
Generate the quiz in the language of the video.
Are the instructions clear to you?"""

        asst_msg1 = "Yes, the instructions are clear!"

        usr_msg2 = """
        Your question should have the following format:

        Question: [the question it self]
        A)Option A
        B)Option B
        C)Option C
        D)Option D
        Answer: [the correct answer]

        Generate the quiz in the language of the video.
        Are the instructions clear to you?
        """

        asst_msg2 = "Yes, I understand the instruction"

        usr_msg3 = """Did you know this about World War II? World War II was one of the deadliest conflicts in human history, lasting from 1939 to 1945. Over 70 million people, or about 3% of the world’s population at the time, lost their lives. The war involved most of the world's nations, including all of the great powers, forming two opposing military alliances: the Allies and the Axis.
        The Allies primarily included the United States, the Soviet Union, the United Kingdom, and China, while the Axis powers were led by Germany, Italy, and Japan. Major events include the invasion of Poland in 1939, which started the war, and the D-Day invasion of Normandy in 1944, which was a turning point for the Allies."""

        asst_msg3 = """ 
        Question: Which event marked the start of World War II?
        A. The bombing of Pearl Harbor
        B. The invasion of Poland
        C. The D-Day invasion
        D. The Battle of Britain
        """

        base_messages = [
            {"role": "user", "content": usr_msg1},
            {"role": "assistant", "content": asst_msg1},
            {"role": "user", "content": usr_msg2},
            {"role": "assistant", "content": asst_msg2},
            {"role": "user", "content": usr_msg3},
            {"role": "assistant", "content": asst_msg3},
        ]

        
