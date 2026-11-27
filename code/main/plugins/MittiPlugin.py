## Mitti entity parser for actions, doers, and receivers
import os 
import spacy
from beans.ActionBean import ActionBean
from beans.TextSentenceBean import TextSentenceBean
from TextToSentenceBreakerPlugin import TextToSentenceBreakerPlugin

class MittiPlugin:


    # Initialize the Mitti entity parser with a document
    def __init__(self, document_str):
        self.list_text_sentence = TextToSentenceBreakerPlugin(document_str).break_into_sentences()
        nlp = spacy.load("en_core_web_trf")
        self.list_sentence = [nlp(sentence.text) for sentence in self.list_text_sentence]

    def _index(self):
        pass

    def get_action_list(self, scene):

        result = []
        for token in scene:
            if token.pos_.casefold() == "VERB".casefold():
                result.append(token)
        
        return result

    def get_main_action(self, scene):
        for token in scene:
            if token.dep_.casefold() == "ROOT".casefold():
                return token
        
        return None

    def get_action_by_text(self, scene, token_text):
        for token in scene:
            if token.text.casefold() == token_text.casefold():
                return token
        
        return None

    
    def is_main_action(self, action):
        return action.dep_.casefold() == "ROOT".casefold()

    def is_aux_action(self, action):
        return action.dep_.casefold() == "aux".casefold()

    def is_present_action(self, action):
        return action.tag_.casefold() == "VBZ".casefold() or action.tag_.casefold() == "VBP".casefold()

    def is_past_action(self, action):
        return action.tag_.casefold() == "VBD".casefold() or action.tag_.casefold() == "VBN".casefold()

    def is_future_action(self, action):
        return action.tag_.casefold() == "MD".casefold()


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
    

    def is_doer_person(self, token):
        return token.ent_type_ == "PERSON" 

    def is_doer_gpe(self, token):
        return token.ent_type_ == "GPE"

    def is_doer_organization(self, token):
        return token.ent_type_ == "ORG" 
        
    def is_doer_location(self, token):
        return token.ent_type_ == "LOC"

    def is_doer_facility(self, token):
        return token.ent_type_ == "FAC"

    def is_doer_product(self, token):
        return token.ent_type_ == "PRODUCT"

    def is_doer_event(self, token):
        return token.ent_type_ == "EVENT"

    def is_doer_work_of_art(self, token):
        return token.ent_type_ == "WORK_OF_ART"

    def is_doer_law(self, token):
        return token.ent_type_ == "LAW"

    def is_doer_language(self, token):
        return token.ent_type_ == "LANGUAGE"

    

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

    
    def get_action_time(self, token_verb):
    
            temp_result = []
            self.result = ""
    
            ## Parse the verb's children to extract day and time information
            for child in token_verb.children:
    
                if child.dep_.casefold() == "npadvmod":
                    temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())
    
                if child.dep_.casefold() == "prep" and child.text.casefold() in {"at", "around", "on"}:                
                    temp_result.append("".join(tok.text_with_ws for tok in child.subtree).strip())
    
            self.result = " ".join(temp_result)
            return self.result