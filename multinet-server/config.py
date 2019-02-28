import os
import sys
import logging
import logging.config
import yaml

def init():
    config = {
        'logging': {
            'level': 'DEBUG'
        }
    }

    MULTINET_SERVER_CONFIG_DIR = os.environ.get('MULTINET_SERVER_CONFIG_DIR', os.path.join('/', 'etc', 'gremlin-server'))
    default_config = os.path.join(MULTINET_SERVER_CONFIG_DIR, 'config.yml')
    default_logging_config = os.path.join(MULTINET_SERVER_CONFIG_DIR, 'logging.conf')

    conf_file = (
        os.environ.get('MULTINET_SERVER_CONF') or
        default_config
    )

    if os.path.exists(conf_file):
        with open(conf_file) as stream:
            config.update(yaml.load(stream))

    logging.basicConfig(stream=sys.stdout, level=logging.getLevelName(config['logging']['level']))
