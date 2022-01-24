# IMPORTS
import os as _os
import sys as _sys
import time as _time
import datetime as _datetime


# CONSTANTS

# Credits
NAME = "MC-Clicker"
AUTHOR = "Nikocraft"
VERSION = "ALPHA-1.1"

# Paths
DATA_PATH = _os.path.abspath("./MC-Clicker_Data")
CONFIG_PATH = f"{DATA_PATH}/config.json"
LOG_PATH = f"{DATA_PATH}/log.txt"

# Log level
LOG_DEBUG = 0
LOG_INFO = 1
LOG_WARNING = 2
LOG_ERROR = 3
LOG_LEVEL_NAMES = {
    LOG_DEBUG: "Debug",
    LOG_INFO: "Info",
    LOG_WARNING: "Warning",
    LOG_ERROR: "Error"
}

# Window
WINDOW_FPS = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 650
WINDOW_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)


# FUNCTIONS

# Wait
def wait(seconds: float):
    _time.sleep(seconds)


# Run time
def run_time():
    return _time.perf_counter()


# Absolut time
def abs_time():
    return _time.time()


# Date and time
def datetime(str_format: str = "%d/%b/%y %H:%M:%S"):
    return _datetime.datetime.now().strftime(str_format)


# Log
def log(message: str, theme: str, level: int):

    # Open the log file
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:

        # Log the message with datetime, name, theme and level to console and log file
        print(f"[{datetime()}] [{NAME} | {theme}] <{LOG_LEVEL_NAMES[level]}> {message}", file=log_file)
        print(f"[{datetime()}] [{NAME} | {theme}] <{LOG_LEVEL_NAMES[level]}> {message}", file=_sys.stdout)
