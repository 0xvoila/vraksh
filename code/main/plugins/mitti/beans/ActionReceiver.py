

class ActionReceiver:

    def __init__(self):
        self.action_receiver_spacy_token = None
        self.receiver_text = None
        self.is_person = False
        self.is_gpe = False
        self.is_organization = False
        self.is_location = False
        self.is_facility = False
        self.is_product = False
        self.is_event = False
        self.is_work_of_art = False
        self.is_law = False
        self.is_language = False

    def set_spacy_token(self, spacy_token):
        self.action_receiver_spacy_token = spacy_token
        self.receiver_text = spacy_token.text
        self.is_person = spacy_token.ent_type_ == "PERSON"
        self.is_gpe = spacy_token.ent_type_ == "GPE"
        self.is_organization = spacy_token.ent_type_ == "ORG"
        self.is_location = spacy_token.ent_type_ == "LOC"
        self.is_facility = spacy_token.ent_type_ == "FAC"
        self.is_product = spacy_token.ent_type_ == "PRODUCT"
        self.is_event = spacy_token.ent_type_ == "EVENT"
        self.is_work_of_art = spacy_token.ent_type_ == "WORK_OF_ART"
        self.is_law = spacy_token.ent_type_ == "LAW"
        self.is_language = spacy_token.ent_type_ == "LANGUAGE"

    
    def from_dict(self, data):
        self.receiver_text = data.get("text")
        self.is_person = data.get("is_person", False)
        self.is_gpe = data.get("is_gpe", False)
        self.is_organization = data.get("is_organization", False)
        self.is_location = data.get("is_location", False)
        self.is_facility = data.get("is_facility", False)
        self.is_product = data.get("is_product", False)
        self.is_event = data.get("is_event", False)
        self.is_work_of_art = data.get("is_work_of_art", False)
        self.is_law = data.get("is_law", False)
        self.is_language = data.get("is_language", False)
        return self

        
    def to_dict(self):
        return {
            "text": self.receiver_text,
            "is_person": self.is_person,
            "is_gpe": self.is_gpe,
            "is_organization": self.is_organization,
            "is_location": self.is_location,
            "is_facility": self.is_facility,
            "is_product": self.is_product,
            "is_event": self.is_event,
            "is_work_of_art": self.is_work_of_art,
            "is_law": self.is_law,
            "is_language": self.is_language
        }
    