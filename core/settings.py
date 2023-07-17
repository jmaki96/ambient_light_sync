""" Defines all common settings across projects and loads all credentials, erroring as appropriate
"""

import datetime
import os


# ========================
# === GENERAL SETTINGS ===
# ========================
DATESTRING = "%m%d%Y_%H%M%S"
DATESTAMP = datetime.datetime.now().strftime(DATESTRING)

# Directories
ROOT_DIRECTORY = os.path.dirname(__file__)

# All files that are generated during runtime are stored in this folder in various subfolders
GENERATED_ASSETS_DIRECTORY = os.path.join(ROOT_DIRECTORY, "generated")
REPORT_DIRECTORY = os.path.join(GENERATED_ASSETS_DIRECTORY, "reports")
LOG_DIRECTORY = os.path.join(GENERATED_ASSETS_DIRECTORY, "logs")
CACHE_DIRECTORY = os.path.join(GENERATED_ASSETS_DIRECTORY, "cache")
TEMP_DIRECTORY = os.path.join(GENERATED_ASSETS_DIRECTORY, "temp")

# Create directories if they don't exist already  (TODO: Should this belong in a different file?)
if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

if not os.path.exists(REPORT_DIRECTORY):
    os.makedirs(REPORT_DIRECTORY)

if not os.path.exists(CACHE_DIRECTORY):
    os.makedirs(CACHE_DIRECTORY)

if not os.path.exists(TEMP_DIRECTORY):
    os.makedirs(TEMP_DIRECTORY)
