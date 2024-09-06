import yaml
from yaml.loader import SafeLoader

from helpers.path_helper import PROJECT_ROOT


class ConfigManager(object):
    config = None

    @classmethod
    def load_config(cls):
        with open(f'{PROJECT_ROOT}/config/config.yaml') as f:
            cls.config = yaml.load(f, Loader=SafeLoader)

    @classmethod
    def get_config(cls) -> dict:
        if not cls.config:
            cls.load_config()
        return cls.config

    @classmethod
    def get_base_url(cls) -> str:
        return cls.get_config()["base_url"]

    @classmethod
    def get_seed(cls) -> str:
        return cls.get_config()["seed"]

    @classmethod
    def get_exercises(cls) -> dict:
        return cls.get_config()["exercises"]

    @classmethod
    def get_exercise(cls, number_of_exercise) -> str:
        return cls.get_exercises()[f'exercise{number_of_exercise}']

