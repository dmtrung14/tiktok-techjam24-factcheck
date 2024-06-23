from transformers import pipeline
from backend.config import Config
import pandas as pd
import csv


class DataBuilder:
    def __init__(self, config = Config.Dataset.BertMNLIYahoo):
        self.config = config
        self.task = self.config.task
        self.model = self.config.model

    def load_data(self):
        pass

    def generate_prompt(self, text):
        classifier = pipeline(self.task, model= self.model)
        hypothesis_template = 'This text is about {}.' # the template used in this demo
        sequence = text
        labels = ['positive', 'negative', 'neutral']
        multi_class = True
        classifier(sequence, labels,
                hypothesis_template=hypothesis_template,
                multi_class=multi_class)

    def label_data(self):
        pass

    def build_data(self):
        self.load_data()
        self.preprocess_data()
        self.label_data()
        self.save_data()
    



if __name__ == "__main__":
    builder = DataBuilder()
    builder.build_data()