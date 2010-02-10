import ConfigParser
import logging
import logging.config
from logging.config import _create_formatters, _install_handlers, _install_loggers

def fileConfig(fnames, defaults=None, disable_existing_loggers=1):
    """
    Read the logging configuration from a ConfigParser-format file.
    """
    cp = ConfigParser.ConfigParser(defaults)
    cp.read(fnames)

    formatters = _create_formatters(cp)

    # critical section
    logging._acquireLock()
    try:
        logging._handlers.clear()
        del logging._handlerList[:]
        # Handlers add themselves to logging._handlers
        handlers = _install_handlers(cp, formatters)

        import inspect
        # we have to do this check because someone got a very lousy patch
        # in late python2.5 that changes the internals of logging we use here.
        # see: http://bugs.python.org/issue3136
        if len(inspect.getargs(_install_loggers.func_code)[0]) == 3:
            _install_loggers(cp, handlers, disable_existing_loggers)
        else:
            _install_loggers(cp, handlers)
    finally:
        logging._releaseLock()
