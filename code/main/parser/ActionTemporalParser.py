import dateparser
import pendulum
from .BaseParser import BaseParser

# VR-3434
class ActionTemporalParser(BaseParser):


    def get_action_time(self, token_verb):

        temp_result = []
        self.result = ""

        ## Parse the verb's children to extract day and time information
        for child in token_verb.children:

            if child.dep_.casefold() == "npadvmod":
                temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())

            if child.dep_.casefold() == "prep" and child.text.casefold() in {"at", "around", "on"}:                
                temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())

        self.result = " ".join(temp_result)
        return self.result
    

    def print(self):
        print(self.result)
    


### Testing 

scene = nlp("Tomorrow , I eat fruits at 12:00 AM")

action_parser = ActionParser()
action_eat = action_parser.get_action_by_text(scene, "eat")

action_time_parser = ActionTemporalParser()
action_time_parser.get_action_time(action_eat)
action_time_parser.print()
action_time_parser.graph(scene)
