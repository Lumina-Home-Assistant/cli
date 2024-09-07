from helpers.module_utils import ModuleUtils

module_utils = ModuleUtils()


class Context:
    def __init__(self):
        pass

    @property
    def pull_all_available_contexts(self) -> str:
        all_modules, path = module_utils.get_all_modules()

        context = """
Here is a list of all modules and what they do. 
Make an accurate decision based off of this. 
If not, respond by prompting the user to either install another module or ask a more specific question.

If you determine a response, you must write python like so
module_name.function_name(parameters, if, required)
        """

        for module_path in all_modules:
            try:
                with open(f"{path}/{module_path}/ai_context.txt") as module_file:
                    content = module_file.read()
                    context += content
            except FileNotFoundError:
                print('Module: ', module_path, ' did NOT contain an `ai_context.txt` file')

        return context
