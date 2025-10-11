import json
import os
import curses
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

#Setting log and checking for todo.json file
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

class Todo:
    self.done= False
    self.data= []
    self.json_read = []
    self.mode= "n"

    def open_todo(self, id):
        with open(APP_PATH, "w") as f:
            self.json_read = json.load(f)

    def save_todo(self):
        with open(APP_PATH, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_todo(self):
        self.data.append({
            "done": False,
            "data": self.data

        })
        self.save_todo()


def main():
    while True:
        setup = FileSetUp()
        app   = Todo()

if __name__ == "__main__":
    main()
