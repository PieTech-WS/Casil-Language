class Code:
    configure_head = {
        "#use": ""
    }

    def __init__(self, source: dict):
        self.source = source
        self.codemap ={}
        for i in self.source.keys():



    def uses(self):
        if "#use" in