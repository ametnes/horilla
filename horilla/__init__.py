"""
init.py
"""

import os
import logging

from horilla import (
    haystack_configuration,
    horilla_apps,
    horilla_context_processors,
    horilla_middlewares,
    horilla_settings,
    rest_conf,
)

ROOT_LOG_LEVEL = os.environ.get("LOG_LEVEL") or "INFO"

PRETTY_LOG_FORMAT = (
    "%(asctime)s.%(msecs)03d [%(levelname)-8s] %(name)+25s - %(message)s"
)
logging.basicConfig(
    level=ROOT_LOG_LEVEL, format=PRETTY_LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S"
)
logging.captureWarnings(True)

