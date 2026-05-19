from functools import wraps

import sys
import logging
import time

LOG = logging.getLogger(__name__)

_LOG_FORMAT = "%(asctime)s :: %(name)-16s :: %(levelname)-5s :: %(message)s"
_LOG_DATEFMT = "%H:%M:%S"

class _Formatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        converter = self.converter(record.created)
        timestamp = time.strftime(datefmt or _LOG_DATEFMT, converter)
        return f"{timestamp}.{int(record.msecs):03d}"

def _input_path() -> str | None:
    if len(sys.argv) < 2 or sys.argv[1].startswith("-"):
        return None
    return sys.argv[1]

def entry_point(foo):
    @wraps(foo)
    def wrapper(*args, **kwargs):
        if _input_path() is None:
            print(
                f"Usage: {sys.argv[0]} <input-file> [--debug]",
                file=sys.stderr,
            )
            sys.exit(1)
        level = logging.INFO
        if "--debug" in sys.argv:
            level = logging.DEBUG
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(_Formatter(_LOG_FORMAT, datefmt=_LOG_DATEFMT))
        logging.basicConfig(level=level, handlers=[handler], force=True)
        start_time = time.time()
        result = foo(*args, **kwargs)
        end_time = time.time()
        LOG.info("Total time in seconds: %s", round((end_time - start_time) * 1000) / 1000)
        return result
    return wrapper
