import pykka
import logging
from mopidy import core

logger = logging.getLogger(__name__)

class FMFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(FMFrontend, self).__init__()
        self.core = core

    # Your frontend implementation

    def on_start(self):
	logger.info("FM Addon started...")

    def on_stop(self):
        logger.info("FM Addon stopped...")

