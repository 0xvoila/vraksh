## Mitti entity parser for actions, doers, and receivers
import os 
import spacy
from plugins.kodak.TextToSentenceBreakerPlugin import TextToSentenceBreakerPlugin
from plugins.mitti.parsers.ActionParser import ActionParser
from plugins.mitti.parsers.ActionDoerParser import ActionDoerParser
from plugins.mitti.parsers.ActionReceiverParser import ActionReceiverParser
from plugins.mitti.beans.Action import Action

from tinydb import TinyDB, where
db = TinyDB('mitti_plugin_db.json')

class MittiPlugin:

    nlp = spacy.load("en_core_web_trf")
    # Initialize the Mitti entity parser with a document
    def __init__(self, document_str):
        self.list_text_sentence = TextToSentenceBreakerPlugin(document_str).break_into_sentences()
        self.list_nlp_sentence = [MittiPlugin.nlp(sentence) for sentence in self.list_text_sentence]

    def _index(self):
        
        for i, sentence in enumerate(self.list_nlp_sentence):
            action_parser = ActionParser()
            action_list = action_parser.get_action_list(sentence)
            for action in action_list:
                doer_list = ActionDoerParser().get_action_doer(action)
                receiver_list = ActionReceiverParser().get_action_receiver(action)
                
                db.insert({
                    'sentence_index': i,
                    'action': action.to_dict() if action else None,
                    'doers': [doer.to_dict() if doer else None for doer in doer_list] if doer_list else None,
                    'receivers': [receiver.to_dict() if receiver else None for receiver in receiver_list] if receiver_list else None
                })