
class Action:
    
    def __init__(self):
        self.action_spacy_token = None
        self.action_lemma = None
        self.action_text = None
        self.is_main = False
        self.is_aux = False
        self.is_present = False
        self.is_past = False
        self.is_future = False

    def set_spacy_token(self, spacy_token):
        self.action_spacy_token = spacy_token
        self.action_lemma = spacy_token.lemma_
        self.action_text = spacy_token.text
        self.is_main = spacy_token.dep_.casefold() == "ROOT".casefold()
        self.is_aux = spacy_token.dep_.casefold() == "aux".casefold()
        self.is_present = spacy_token.tag_.casefold() == "VBZ".casefold() or spacy_token.tag_.casefold() == "VBP".casefold()
        self.is_past = spacy_token.tag_.casefold() == "VBD".casefold() or spacy_token.tag_.casefold() == "VBN".casefold()
        self.is_future = spacy_token.tag_.casefold() == "MD".casefold()

    ## List of getters for action properties
    def get_spacy_token(self):
        return self.action_spacy_token
    
    def get_action_lemma(self):
        return self.action_lemma

    def get_action_text(self):
        return self.action_text

    def get_is_main(self):
        return self.is_main

    def get_is_aux(self):
        return self.is_aux

    def get_is_present(self):
        return self.is_present

    def get_is_past(self):
        return self.is_past

    def get_is_future(self):
        return self.is_future

    def from_dict(self, data):
        self.action_text = data.get("text")
        self.action_lemma = data.get("lemma")
        self.is_main = data.get("is_main", False)
        self.is_aux = data.get("is_aux", False)
        self.is_present = data.get("is_present", False)
        self.is_past = data.get("is_past", False)
        self.is_future = data.get("is_future", False)
        return self
    
    def to_dict(self):
        return {
            "text": self.action_text,
            "lemma": self.action_lemma,
            "is_main": self.is_main,
            "is_aux": self.is_aux,
            "is_present": self.is_present,
            "is_past": self.is_past,
            "is_future": self.is_future
        }
