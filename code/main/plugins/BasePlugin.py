import spacy
from spacy import displacy

class BasePlugin:

    def __init__(self):
        self.nlp_model = spacy.load("en_core_web_trf")
    
    def nlp(self, scene_str):
        return self.nlp_model(scene_str)

    def perform(self):
        print("Override this method to perform the job and return data")
        
    def print(self):
        print("Override this method to print the results")
    
    def graph(self, scene):
        displacy.render(scene, style="dep", jupyter=True)
        