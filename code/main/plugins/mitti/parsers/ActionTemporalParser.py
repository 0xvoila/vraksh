import dateparser
import pendulum
from plugins.mitti.beans.ActionTime import ActionTime
from plugins.mitti.beans.Action import Action


# VR-3434
class ActionTemporalParser():


    def get_action_time(self, token_verb: Action):

        temp_result = []
        self.result = ""

        ## Parse the verb's children to extract day and time information
        for child in token_verb.get_spacy_token().children:

            if child.dep_.casefold() == "npadvmod":
                temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())

            if child.dep_.casefold() == "prep" and child.text.casefold() in {"at", "around", "on"}:                
                temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())

        self.result = " ".join(temp_result)
        action_time = ActionTime()
        action_time.set_action_time(self.result)
        return action_time
    

    def print(self):
        print(self.result)
    


### Testing 

# scene = nlp("Tomorrow , I eat fruits at 12:00 AM")

# action_parser = ActionParser()
# action_eat = action_parser.get_action_by_text(scene, "eat")

# action_time_parser = ActionTemporalParser()
# action_time_parser.get_action_time(action_eat)
# action_time_parser.print()
# action_time_parser.graph(scene)
