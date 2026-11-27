from plugins.mitti.beans.ActionDoer import ActionDoer
from plugins.mitti.beans.Action import Action

# VR-4323
class ActionDoerParser():


    def get_action_doer(self, token_verb: Action):

        result = []

        for token in token_verb.get_spacy_token().children:

            if token.dep_.casefold() == "nsubj".casefold():
                result.append(ActionDoer().set_spacy_token(token))

        return result

    def get_action_doer_by_text(self, token_verb: Action, token_text: str):
        result = []

        for token in token_verb.get_spacy_token().children:

            if token.dep_.casefold() == "nsubj".casefold() and token.text.casefold() == token_text.casefold():
                result.append(ActionDoer().set_spacy_token(token))

        return result





### Testing 

# scene = nlp("Amit eats fruits")
# action_doer_parser = ActionDoerParser()
# action_parser = ActionParser()
# action_eat = action_parser.get_action_by_text(scene, "eats")
# action_doer_amit = action_doer_parser.get_action_doer_by_text(action_eat, "Amit")[0]
# assert action_doer_parser.is_person(action_doer_amit) == True

# scene = nlp("India does good job")
# action_doer_parser = ActionDoerParser()
# action_parser = ActionParser()
# action_does = action_parser.get_action_by_text(scene, "does")
# action_doer_india = action_doer_parser.get_action_doer_by_text(action_does, "India")[0]
# assert action_doer_parser.is_gpe(action_doer_india) == True

# action_doer_parser = ActionDoerParser()
# scene = action_doer_parser.nlp("Amit drinks juice")
# action_doer_parser.graph(scene)
