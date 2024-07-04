import configparser
from pathlib import Path


def read_config(section, key):
    config = configparser.ConfigParser()
    project_path = Path(__file__).parent.parent.parent
    config.read(str(project_path) + '/config/test_config.ini')
    return config[section][key]
