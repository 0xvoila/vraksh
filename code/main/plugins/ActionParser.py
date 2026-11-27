from BaseParser import BaseParser

class ActionParser(BaseParser):

    def get_action_list(self, scene):

        result = []
        for token in scene:
            if token.pos_.casefold() == "VERB".casefold():
                result.append(token)
        
        return result

    def get_main(self, scene):
        for token in scene:
            if token.dep_.casefold() == "ROOT".casefold():
                return token
        
        return None

    def get_action_by_text(self, scene, token_text):
        for token in scene:
            if token.text.casefold() == token_text.casefold():
                return token
        
        return None

    
    def is_main(self, action):
        return action.dep_.casefold() == "ROOT".casefold()

    def is_aux(self, action):
        return action.dep_.casefold() == "aux".casefold()

    def is_present(self, action):
        return action.tag_.casefold() == "VBZ".casefold() or action.tag_.casefold() == "VBP".casefold()

    def is_past(self, action):
        return action.tag_.casefold() == "VBD".casefold() or action.tag_.casefold() == "VBN".casefold()

    def is_future(self, action):
        return action.tag_.casefold() == "MD".casefold()
        


### Testing 
action_parser = ActionParser()
scene = action_parser.nlp("Sunday, I eat fruits and drink water at 12:00 midnight")
action_list = action_parser.get_action_list(scene)

assert len(action_list) == 2
assert action_parser.get_main(scene).text == "eat"
assert action_parser.get_action_by_text(scene, "eat").text == "eat"

token_eat = action_parser.get_action_by_text(scene, "eat")
assert action_parser.is_present(token_eat) == True