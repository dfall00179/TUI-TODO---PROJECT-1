import json
import os
import datetime
import logging as log

from dataclasses  import dataclass

from rich.console  import Console
from rich.table    import Table
from rich.markdown import Markdown

console = Console()

# console.print(dir(os))
HOME_DIR  = os.environ.get("HOME")
APP_DIR   = os.path.join(HOME_DIR, ".TODO")
APP_PATH  = os.path.join(APP_DIR, "todo.json")

log.basicConfig(
    filename='app.log',
    level=log.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class FileSetUp:
    logging.info("\n" + "="*60)
    logging.info("New Execution")
    logging.info("="*60 + "\n")

    def __init__(self):
        if os.path.exists(APP_PATH):
            log.info("file already there")

        else:
            log.warning("no todo.json file")
            os.makedirs(APP_DIR, exist_ok=True)

            with open(APP_PATH, "w") as f:
                json.dump([], f)

            log.info("file created")

def main():
    setup = FileSetUp()

if __name__ == "__main__":
    main()
