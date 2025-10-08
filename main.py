import json
import os
import time
import logging as log

from rich.console  import Console
from rich.table    import Table
from rich.markdown import Markdown

# console.print(dir(os))
HOME_DIR  = os.environ.get("HOME")
APP_DIR   = os.path.join(HOME_DIR, ".TODO")
APP_PATH  = os.path.join(APP_DIR, "todo.json")

log.basicConfig(
    filename='app.log',
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

console = Console()

class FileSetUp:
    log.info("="*30)
    log.info("New Execution")
    log.info("="*30 + "\n")

    def __init__(self):
        if os.path.exists(APP_PATH):
            log.info("file already there")

        else:
            log.warning("no todo.json file")
            os.makedirs(APP_DIR, exist_ok=True)

            with open(APP_PATH, "w") as f:
                json.dump([], f)

            log.info("file created")

class Task:
    def __init__(self, id, data, done=False):
        self.id   = id
        self.data = data
        self.done = done


def main():
    while True:
        setup = FileSetUp()

if __name__ == "__main__":
    main()
