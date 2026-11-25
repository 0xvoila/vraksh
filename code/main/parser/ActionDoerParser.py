from BaseParser import BaseParser

# VR-4323
class ActionDoerParser(BaseParser):


    def get_action_doer(self, token_verb):

        result = []

        for token in token_verb.children:

            if token.dep_.casefold() == "nsubj".casefold():
                result.append(token)

        return result

    def get_action_doer_by_text(self, token_verb, token_text):
        result = []

        for token in token_verb.children:

            if token.dep_.casefold() == "nsubj".casefold() and token.text.casefold() == token_text.casefold():
                result.append(token)

        return result
    

    def is_person(self, token):
        return token.ent_type_ == "PERSON" 

    def is_gpe(self, token):
        return token.ent_type_ == "GPE"

    def is_organization(self, token):
        return token.ent_type_ == "ORG" 
        
    def is_location(self, token):
        return token.ent_type_ == "LOC"

    def is_facility(self, token):
        return token.ent_type_ == "FAC"

    def is_product(self, token):
        return token.ent_type_ == "PRODUCT"

    def is_event(self, token):
        return token.ent_type_ == "EVENT"

    def is_work_of_art(self, token):
        return token.ent_type_ == "WORK_OF_ART"

    def is_law(self, token):
        return token.ent_type_ == "LAW"

    def is_language(self, token):
        return token.ent_type_ == "LANGUAGE"




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

action_doer_parser = ActionDoerParser()
scene = action_doer_parser.nlp("Amit drinks juice")
action_doer_parser.graph(scene)
