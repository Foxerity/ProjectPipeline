from DataSetsProcess import DataSetsProcess
from ModelControl import ModelControl
from PreProcess import PreProcess
from VisualProcess import VisualProcess
from pipeline_abc import Pipeline


class MainProject(Pipeline):
    def __init__(self):
        super().__init__()
        self.PreProcess = None

    def setup(self, **kwargs):
        self.config = {
            'name': 'MainProject'
        }

        self.modules = [
            PreProcess(),
            DataSetsProcess(),
            ModelControl(),
            VisualProcess()
        ]

        self.initialize_modules()

        self.PreProcess.run()

        for module in self.modules:
            module.setup()
            module.save_configfile(f"{module.__class__.__name__}.yaml")

    def run(self, **kwargs):
        for module in self.modules[2:3]:
            module.run()


if __name__ == '__main__':
    main = MainProject()
    main.save_configfile(f'{main.__class__.__name__}.yaml')
    main.setup()
    main.run()

    # main = MainProject()
    # main.from_configfile([
    #                         'MainProject.yaml',
    #                         'PreProcess.yaml',
    #                         'DataSetsProcess.yaml',
    #                         'ModelControl.yaml',
    #                         'VisualProcess.yaml'
    #                       ])
    # main.run()


