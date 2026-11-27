import os 
import sys


import dateparser
import pendulum 
import ActionParser, ActionDoerParser, BaseParser
from jinja2 import Template

class Engine(BaseParser):
    
    def __init__(self):
        self.graph = nx.DiGraph()
        super().__init__()

    
    def _add_scene(self, scene):
        action_parser = ActionParser()
        action_main = action_parser.get_main(self.nlp(scene))

        action_doer_parser = ActionDoerParser()
        action_main_doer = action_doer_parser.get_action_doer(action_main)
        self.prepare_summary_data(action_main_doer[0].text.strip(), action_main.text)

    def add_subject(self, subject):
        self.graph.add_node(subject, type="subject")

    
    def add_subject_action_rel(self, subject, action):
        self.graph.add_edge(subject, action, type="subject_action")
        
    def add_action(self, action):
        self.graph.add_node(action, type="action")

## Testing 
if __name__ == "__main__":
    summary = SimpleSummary()
    summary.add_scene("Amit eats fruits")
    summary.add_scene("Amit drinks juice")
    summary.add_scene("Rahul goes to office")
    print(summary.summarize())
