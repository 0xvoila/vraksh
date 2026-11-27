from plugins.mitti.parsers.ActionParser import ActionParser
from plugins.mitti.beans.Action import Action
from plugins.mitti.beans.ActionReceiver import ActionReceiver

# VR-1212
class ActionReceiverParser():

    def get_action_receiver(self, token_action : Action):
    
        result = []
    
        for token in token_action.get_spacy_token().children:

            ## Now check if this action has any direct object which is non living
            if (token.dep_.casefold() == "dobj"):
                result.append(ActionReceiver().set_spacy_token(token))

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
                result.append(ActionReceiver().set_spacy_token(prep_obj_list[0]))

        return result


### Testing 
# action_parser = ActionParser()
# scene = action_parser.nlp("I am playing with my calculator which is placed on the table")
# action_token_playing = action_parser.get_action_by_text(scene, "playing")

# action_receiver_parser = ActionReceiverParser()
# result = action_receiver_parser.get_action_receiver(action_token_playing)
# assert result[0].text == "calculator" 

# scene = action_parser.nlp("I am going to school")
# action_parser = ActionParser()
# action_token_going = action_parser.get_action_by_text(scene, "going")

# action_receiver_parser = ActionReceiverParser()
# result = action_receiver_parser.get_action_receiver(action_token_going)
# assert result[0].text == "school"

# scene = action_parser.nlp("I am playing cricket in the ground")
# action_parser = ActionParser()
# action_token_playing = action_parser.get_action_by_text(scene, "playing")

# action_receiver_parser = ActionReceiverParser()
# result = action_receiver_parser.get_action_receiver(action_token_playing)
# assert result[0].text == "cricket", "FAILED" 