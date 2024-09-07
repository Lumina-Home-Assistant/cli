import os


class ModuleUtils:
    def __init__(self, module_path='./modules/'):
        self.module_path = module_path

    def get_all_modules(self) -> list:
        directories = [
            name for name in os.listdir(self.module_path) if os.path.isdir(os.path.join(self.module_path, name))
        ]
        return directories, self.module_path
