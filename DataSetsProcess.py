from pipeline_abc import Pipeline


class DataSetsProcess(Pipeline):
    def __init__(self):
        super().__init__()
        pass

    def setup(self, **kwargs):
        self.config = {
            "name": 'DataSetsProcess'
        }
        self.modules = [

        ]

    def run(self, callbacks=None, **kwargs):
        pass

