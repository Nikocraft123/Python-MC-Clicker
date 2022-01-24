# IMPORTS
import os
import sys
from general import *


# CLASSES

# App
class App:

    # CONSTRUCTOR
    def __init__(self):
        pass


    # METHODS

    # Run
    def run(self):
        self.quit()

    # Quit
    def quit(self):

        # Exit program
        log("Quit application ...", "MAIN", LOG_INFO)
        sys.exit(0)


# FUNCTIONS

# Main
def main():

    # Print header
    print(NAME)
    print("-" * len(NAME))
    print("")
    print(f"Author: {AUTHOR}")
    print(f"Version: {VERSION}")
    print("")

    # Set up the data directory with a log file
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    with open(LOG_PATH, "w", encoding="utf-8") as log_file:
        log_file.write(NAME + "\n")
        log_file.write("-" * len(NAME) + "\n")
        log_file.write("\n")
        log_file.write(f"Author: {AUTHOR}" + "\n")
        log_file.write(f"Version: {VERSION}" + "\n")
        log_file.write("\n")

    # Initialize the application
    log("Initialize application ...", "MAIN", LOG_INFO)
    app = App()

    # Run the application
    log("Run application ...", "MAIN", LOG_INFO)
    app.run()


# MAIN
if __name__ == '__main__':
    main()
