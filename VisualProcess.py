from pipeline_abc import Pipeline


class VisualProcess(Pipeline):
    def __init__(self):
        super().__init__()
        pass

    def setup(self, **kwargs):
        self.config = {
            "name": 'VisualProcess'
        }

        self.modules = [

        ]

