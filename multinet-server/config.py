import os
import sys
import logging
import logging.config
import yaml

def init():
    MULTINET_SERVER_CONFIG_DIR = os.environ.get('MULTINET_SERVER_CONFIG_DIR', os.path.join('/', 'etc', 'gremlin-server'))
    default_config = os.path.join(MULTINET_SERVER_CONFIG_DIR, 'config.yml')
    default_logging_config = os.path.join(MULTINET_SERVER_CONFIG_DIR, 'logging.conf')

    conf_file = (
        os.environ.get('MULTINET_SERVER_CONF') or
        default_config
    )

    if os.path.exists(conf_file):
        with open(conf_file) as stream:
            config = yaml.load(stream)
    else:
        config = {
            'logging': {
                'config': None
            }
        }

    log_conf_file = (
        config['logging']['config'] or
        os.environ.get('MULTINET_SERVER_LOG_CONF') or
        default_logging_config
    )

    if os.path.exists(log_conf_file):
        logging.config.fileConfig(log_conf_file)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
