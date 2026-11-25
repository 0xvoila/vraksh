from .BaseParser import BaseParser

# VR-1212
class ActionReceiverParser(BaseParser):


    def get_action_receiver(self, token_action):
    
        result = []
    
        for token in token_action.children:

            ## Now check if this action has any direct object which is non living
            if (token.dep_.casefold() == "dobj"):
                result.append(token)

            ## We have to handle the cases when object is not direct object and living object
            if (token.dep_.casefold() == "prep"):
                result.extend(self._parse_prep(token))


        return result


    # In this method we will evaluate if object could be the prep object
    def _parse_prep(self, token):

        result = []

        if (token.text.casefold() == "with") or (token.text.casefold() == "to"):

            prep_obj_list = [child for child in token.children if child.dep_.casefold() == "pobj"]
            if list(prep_obj_list):
                result.append(prep_obj_list[0])

        return result


### Testing 

scene = nlp("I am playing with my calculator which is placed on the table")
action_parser = ActionParser()
action_token_playing = action_parser.get_action_by_text(scene, "playing")

action_receiver_parser = ActionReceiverParser()
result = action_receiver_parser.get_action_receiver(action_token_playing)
assert result[0].text == "calculator" 

scene = nlp("I am going to school")
action_parser = ActionParser()
action_token_going = action_parser.get_action_by_text(scene, "going")

action_receiver_parser = ActionReceiverParser()
result = action_receiver_parser.get_action_receiver(action_token_going)
assert result[0].text == "school"

scene = nlp("I am playing cricket in the ground")
action_parser = ActionParser()
action_token_playing = action_parser.get_action_by_text(scene, "playing")

action_receiver_parser = ActionReceiverParser()
result = action_receiver_parser.get_action_receiver(action_token_playing)
assert result[0].text == "cricket", "FAILED" 