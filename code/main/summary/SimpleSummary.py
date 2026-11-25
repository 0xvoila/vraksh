import dateparser
import pendulum 
from parser import ActionParser, ActionDoerParser, BaseParser
from jinja2 import Template

class SimpleSummary(BaseParser):
    
    def __init__(self):
        self.subject_action_data = {}
        self.scene_list = []
        super().__init__()
        self.template_str = """
        
        Following actions has been taken 

        {% for subject, actions in subject_actions.items() -%}
        - {{ subject }}
            {% for action in actions -%}
            - {{ action }}
            {% endfor %}
        {% endfor %}
    
    """

    def add_scene(self, scene_str):
        self.scene_list.append(self.nlp(scene_str))

    def summarize(self):
        template = Template(self.template_str)

        for scene in self.scene_list:
            action_parser = ActionParser()
            action_main = action_parser.get_main(scene)

            action_doer_parser = ActionDoerParser()
            action_main_doer = action_doer_parser.get_action_doer(action_main)
            self.prepare_summary_data(action_main_doer[0].text.strip(), action_main.text)

        return template.render(subject_actions=self.subject_action_data)


    def prepare_summary_data(self, subject, action):

        if subject not in self.subject_action_data:
            self.subject_action_data[subject] = []
        self.subject_action_data[subject].append(action)



## Testing 
if __name__ == "__main__":
    summary = SimpleSummary()
    summary.add_scene("Amit eats fruits")
    summary.add_scene("Amit drinks juice")
    summary.add_scene("Rahul goes to office")
    print(summary.summarize())
