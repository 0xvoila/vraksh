class DataPlugin:
    def __init__(self):
        pass

    def spacy_data(self, spacy_token):
        self.spacy_token = spacy_token
    
    def data(self, data):
        self.data = data


    def get_data(self):
        if hasattr(self, 'spacy_token') and self.spacy_token is not None:
            return self.spacy_token         
        if hasattr(self, 'data'):
            return self.data
        return None