import pandas as pd

class DataBuilder:
    def __init__(self, data_path: str, data: pd.DataFrame):
        self.data_path = data_path
        self.data = data

    def load_data(self):
        pass

    def preprocess_data(self):
        pass

    def label_data(self):
        pass

    def build_data(self):
        pass


if __name__ == "__main__":
    builder = DataBuilder()
    builder.build_data()