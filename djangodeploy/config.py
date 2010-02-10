import imp
import hashlib
import os

# Create a namespace in which to load configs
def load_config(name, path, dictionary, required=True):
    package = hashlib.md5('%s%s' % (path, name)).hexdigest()
    fp = None
    try:
        fp, pathname, description = imp.find_module(name, [path])
    except ImportError:
        if required:
            raise
    else:
        config = imp.load_module(package, fp, pathname, description)
        dictionary.update(dict([ (k, v) for k, v in config.__dict__.items() if k.isupper() ]))
    finally:
        if fp:
            fp.close()
