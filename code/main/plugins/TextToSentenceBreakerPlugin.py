import re
from beans.TextSentenceBean import TextSentenceBean

class TextToSentenceBreakerPlugin:
    def __init__(self, text):
        self.text = text
    
    def break_into_sentences(self):
        return [TextSentenceBean(sentence) for sentence in re.split(r'(?<=[.!?]) +', self.text)]