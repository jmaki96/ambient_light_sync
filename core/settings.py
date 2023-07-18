""" Defines all common settings across projects
"""

import datetime
import os


# ========================
# === GENERAL SETTINGS ===
# ========================
APP_NAME = 'ambient_light_sync'

DATESTRING = "%m%d%Y_%H%M%S"
DATESTAMP = datetime.datetime.now().strftime(DATESTRING)

# Directories
ROOT_DIRECTORY = os.path.dirname(__file__)

CERTIFICATE_DIRECTORY = os.path.join(os.path.dirname(ROOT_DIRECTORY), 'certificates')

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


# ====================
# === HUE SETTINGS ===
# ====================
HUE_BRIDGE_ADDRESS = os.environ.get('HUE_BRIDGE_ADDRESS')
HUE_BRIDGE_CERTIFICATE_PATH = os.path.join(CERTIFICATE_DIRECTORY, 'hue_bridge_certificate.pem')
