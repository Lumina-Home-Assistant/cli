import requests
import subprocess
from pydoc import locate

class Installations:
    def __init__(self):
        pass

    def check_repo(self, repo_url) -> bool:
        # if returns false, then url is NOT valid to clone and exit with error
        resp = requests.get(repo_url)
        return True if resp.status_code == 200 else False

    def get_module_name(self, repo_url) -> str:
        split: list = repo_url.split('/')
        return split[-1]

    def clone_repo(self, repo_url, clone_to_path='./modules') -> None:
        module_name = self.get_module_name(repo_url)
        try:
            subprocess.run(['git', 'clone', repo_url, f"{clone_to_path}/{module_name}"], check=True)
            print(f"Repository cloned to {clone_to_path}")
            self.check_repo(repo_url)
        except subprocess.CalledProcessError as e:
            raise subprocess.CalledProcessError(f"Failed to clone repository: {e}")

    def check_installation(self, module_name) -> bool:
        import_class = locate(f'{module_name}.app.{module_name}')
        if not import_class:
            raise ModuleNotFoundError(f"Module {module_name} not found")

        try:
            with open(f"./modules/{module_name}/ai_context.txt"):
                pass
        except FileNotFoundError:
            print('Module: ', module_name, ' did NOT contain an `ai_context.txt` file')
            # doesn't throw error but prints warning
