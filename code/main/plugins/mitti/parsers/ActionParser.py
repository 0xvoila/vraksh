from plugins.mitti.beans.Action import Action

class ActionParser():

    def get_action_list(self, scene):

        result = []
        for token in scene:
            if token.pos_.casefold() == "VERB".casefold():
                action = Action()
                action.set_spacy_token(token)
                result.append(action)
        
        return result

    def get_main(self, scene):
        for token in scene:
            if token.dep_.casefold() == "ROOT".casefold():
                return Action().set_spacy_token(token)
        
        return None

    def get_action_by_text(self, scene, token_text):
        for token in scene:
            if token.text.casefold() == token_text.casefold():
                return Action().set_spacy_token(token)
        
        return None
        


### Testing 
# action_parser = ActionParser()
# scene = action_parser.nlp("Sunday, I eat fruits and drink water at 12:00 midnight")
# action_list = action_parser.get_action_list(scene)

# assert len(action_list) == 2
# assert action_parser.get_main(scene).text == "eat"
# assert action_parser.get_action_by_text(scene, "eat").text == "eat"

# token_eat = action_parser.get_action_by_text(scene, "eat")
# assert action_parser.is_present(token_eat) == True