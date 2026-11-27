
class ActionTime:

    def set_action_time(self, action_time):
        self.action_time = action_time

    def from_dict(self, data):
        self.action_time = data.get("action_time")
        return self

    def to_dict(self):
        return {
            "action_time": self.action_time
        }
