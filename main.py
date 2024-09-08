from helpers.context import Context
from helpers.installations import Installations

context = Context()
mod_install = Installations()

print(context.pull_all_available_contexts)

def main(cmd: str, dev: bool = False):
    """
    :param cmd: Command to be executed
    :param dev: Developer flags
    :return:
    """
    if cmd == 'install':
        url = input("Github Repository URL: ")
        if mod_install.check_repo(url):
            mod_install.clone_repo(url)
        else:
            return 0


if __name__ == '__main__':
    cmd = input(": ")
    main(cmd)
