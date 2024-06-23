import json
from TikTokApi import TikTokApi
from transformers import pipeline
from config import Config
import torch
import pandas as pd
import numpy as np
import csv
import re


class DataBuilder:
    def __init__(self, config = Config.Dataset.BertMNLIYahoo):
        self.config = config
        self.task = self.config.task
        self.model = self.config.model
        self.data = pd.DataFrame()
        self.data_dict = dict()
        self.videos = self.config.videos
        self.labels = self.config.labels

    def extract_text(self, text):
        # Remove hashtags
        text = re.sub(r'#\w+', '', text)
        # Remove @ tags
        text = re.sub(r'@\w+', '', text)
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        # Remove any character not in a-z A-Z 0-9
        text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
        return text
    
    def _one_hot_tags(self, video):
        vector = [0] * len(self.hashtags)
        for challenge in video['challenges']:
            if challenge in self.hashtags:
                vector[self.hashtags.index(challenge)] = 1
        
        return vector
    
    def reorder_labels(self, og_labels, results):
        new_labels = [0 * len(og_labels)]
        for result in results:
            scores = result['scores']
            labels = result['labels']
            this_labels = []
            for label in og_labels:
                index = labels.index(label)
                this_labels.append(scores[index])
            for i in range(len(this_labels)):
                if this_labels[i] > new_labels[i]:
                    new_labels[i] = this_labels[i]
        return new_labels
    
    def vectorize_desc(self, text):
        classifier = pipeline(self.task, model= self.model, device=0 if torch.cuda.is_available() else -1)
        hypothesis_template = 'This text is about {}.' # the template used in this demo
        sequence = [text]
        labels = self.config.topics
        multi_class = True
        # get the topic of the description
        topics = classifier(sequence, labels,
                hypothesis_template=hypothesis_template,
                multi_class=multi_class)
        topics = self.reorder_labels(self.config.topics, topics)

        # get the sentiment of the description
        hypothesis_template = 'The sentiment of this text is {}.'
        labels = self.config.sentiments
        sentiments = classifier(sequence, labels,
                hypothesis_template=hypothesis_template,
                multi_class=multi_class)
        sentiments = self.reorder_labels(self.config.sentiments, sentiments)
        return  topics + sentiments
        
    def vectorize_challenges(self, challenges):
        classifier = pipeline(self.task, model= self.model, device=0 if torch.cuda.is_available() else -1)
        hypothesis_template = 'This text is about {}.'
        sequence = challenges
        labels = self.config.topics
        multi_class = True
        # get the topic of the description
        topics = classifier(sequence, labels,
                hypothesis_template=hypothesis_template,
                multi_class=multi_class)
        topics = self.reorder_labels(self.config.topics, topics)
        
        # get the sentiment of the description
        hypothesis_template = 'The sentiment of this text is {}.'
        labels = self.config.sentiments
        sentiments = classifier(sequence, labels,
                hypothesis_template=hypothesis_template,
                multi_class=multi_class)
        sentiments = self.reorder_labels(self.config.sentiments, sentiments)
        return  topics + sentiments
        
    def preprocess_data(self):
        count = 0
        for video_id in self.videos:
            print(f'Processing video {count} of {len(self.videos)}')
            video = self.videos[video_id]
            text = self.extract_text(video['desc'])
            # vectorize the description by topics and semantics
            desc_vector = self.vectorize_desc(text)
            # vectorize the challenges (tags) by topics and semantics
            challenge_vector = self.vectorize_challenges(video['challenges'])
            # one hot encode the tags
            tag_vector = self._one_hot_tags(video)

            # add the item to the data dictionary
            self.data_dict[video_id] = desc_vector + challenge_vector + tag_vector 
            count += 1
    def label_data(self):
        pass

    def save_data(self):
        with open('data/data.json', 'w') as f:
                    json.dump(self.data_dict, f, indent=4)
        

    def build_data(self):
        self.preprocess_data()
        self.save_data()
        
    



if __name__ == "__main__":
    builder = DataBuilder()
    builder.build_data()