# Lumina Home Assistant Command Line Interface

## Create a module

- Include a `requirements.txt` file if dependencies are needed
- Include an `ai_context.txt` file, otherwise your module will not be used. *An example is listed below*
- Your main class should be listed within `app.py`, otherwise it cannot be found
- the class should also be the same name as the GitHub project repository name (see example below)

You can include other files in your project, just note the get run in the `main.py` in the project root! Build with that in mind, when handling imports.

### How we clone?
- A user is initially prompted to provide a GitHub url
- The URL is checked to make sure it exists
- The URL is parsed and the repository name, becomes the module name.
- **Make your names unique, to prevent potential conflicts!**

## Examples

`<module_name>/ai_context.txt` example. It is recommended to use this format.  
```text
# This module (called "time") contains everything time related, here is a list of all functions and their purpose:

## function current_time:
- Params: None
- Returns: The current time as (hh:mm AM/PM)

## function current_date:
- Params: None
- Returns: The current date as (Y:m:d)
```

`<module_name>/app.py` example. You MUST follow this format to prevent errors.
```python
# module name is 'time' (matches classname)
from datetime import datetime


class time:
    def __init__(self):
        pass

    # Function to get current time as (hh:mm AM/PM)
    def current_time(self):
        return datetime.now().strftime("%I:%M %p")

    # Function to get current date as (Y:m:d)
    def current_date(self):
        return datetime.now().strftime("%Y:%m:%d")
```