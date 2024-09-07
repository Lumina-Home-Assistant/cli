from helpers.context import Context

context = Context()

print(context.pull_all_available_contexts)


def main(cmd: str, dev: bool = False):
    """
    :param cmd: Command to be executed
    :param dev: Developer flags
    :return:
    """
