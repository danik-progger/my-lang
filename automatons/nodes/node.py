class AutomatonNode:
    def __init__(self):
        self.to = dict()
        self.terminal = set()

    def make_terminal(self, token: str):
        self.terminal.add(token)
