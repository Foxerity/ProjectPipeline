from pipeline_abc import Pipeline


class PreProcess(Pipeline):
    def __init__(self):
        super().__init__()
        pass

    def setup(self, **kwargs):
        self.config = {
            "name": 'PreProcess'
        }

        self.modules = [

        ]

    def run(self, callbacks=None, **kwargs):
        print("PreProcess: I'm PreProcess.")
