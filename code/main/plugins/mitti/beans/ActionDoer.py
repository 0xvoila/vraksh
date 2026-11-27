

class ActionDoer:

    def __init__(self):
        self.action_doer_spacy_token = None

    def set_spacy_token(self, spacy_token):
        self.action_doer_spacy_token = spacy_token
        self.is_person()
        self.is_gpe()
        self.is_organization()
        self.is_location()
        self.is_facility()
        self.is_product()
        self.is_event()
        self.is_work_of_art()
        self.is_law()
        self.is_language()

    def is_person(self):
        return self.action_doer_spacy_token.ent_type_ == "PERSON" 

    def is_gpe(self):
        return self.action_doer_spacy_token.ent_type_ == "GPE"

    def is_organization(self):
        return self.action_doer_spacy_token.ent_type_ == "ORG" 
        
    def is_location(self):
        return self.action_doer_spacy_token.ent_type_ == "LOC"

    def is_facility(self):
        return self.action_doer_spacy_token.ent_type_ == "FAC"

    def is_product(self):
        return self.action_doer_spacy_token.ent_type_ == "PRODUCT"

    def is_event(self):
        return self.action_doer_spacy_token.ent_type_ == "EVENT"

    def is_work_of_art(self):
        return self.action_doer_spacy_token.ent_type_ == "WORK_OF_ART"

    def is_law(self):
        return self.action_doer_spacy_token.ent_type_ == "LAW"

    def is_language(self):
        return self.action_doer_spacy_token.ent_type_ == "LANGUAGE"


    def get_entity_type(self):
        return self.action_doer_spacy_token.ent_type_
    

    def to_dict(self):
        return {
            "text": self.action_doer_spacy_token.text,
            "entity_type": self.get_entity_type()
        }
    