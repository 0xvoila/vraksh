
class Action:
    
    def set_spacy_token(self, spacy_token):
        self.action_spacy_token = spacy_token
        self.action_lemma()
        self.action_text()
        self.is_main()
        self.is_aux()
        self.is_present()
        self.is_past()
        self.is_future()

    ## List of setters for action properties
    def action_lemma(self):
        return self.action_spacy_token.lemma_

    def action_text(self):
        return self.action_spacy_token.text

    def is_main(self):
        return self.action_spacy_token.dep_.casefold() == "ROOT".casefold()

    def is_aux(self):
        return self.action_spacy_token.dep_.casefold() == "aux".casefold()

    def is_present(self):
        return self.action_spacy_token.tag_.casefold() == "VBZ".casefold() or self.action_spacy_token.tag_.casefold() == "VBP".casefold()

    def is_past(self):
        return self.action_spacy_token.tag_.casefold() == "VBD".casefold() or self.action_spacy_token.tag_.casefold() == "VBN".casefold()

    def is_future(self):
        return self.action_spacy_token.tag_.casefold() == "MD".casefold()


    ## List of getters for action properties
    def get_spacy_token(self):
        return self.action_spacy_token
    
    def get_action_lemma(self):
        return self.action_lemma()

    def get_action_text(self):
        return self.action_text()

    def get_is_main(self):
        return self.is_main()

    def get_is_aux(self):
        return self.is_aux()

    def get_is_present(self):
        return self.is_present()

    def get_is_past(self):
        return self.is_past()

    def get_is_future(self):
        return self.is_future()

    def get_to_dict(self):
        return self.to_dict()
    
    def to_dict(self):
        return {
            "text": self.action_text(),
            "lemma": self.action_lemma(),
            "is_main": self.is_main(),
            "is_aux": self.is_aux(),
            "is_present": self.is_present(),
            "is_past": self.is_past(),
            "is_future": self.is_future()
        }
