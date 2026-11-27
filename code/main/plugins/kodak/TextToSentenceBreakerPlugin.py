import re

class TextToSentenceBreakerPlugin:
    def __init__(self, text):
        self.text = text
    
    def break_into_sentences(self):
        return [sentence for sentence in re.split(r'(?<=[.!?]) +', self.text)]