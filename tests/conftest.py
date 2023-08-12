import os
import pytest
import dotenv
from dotenv import load_dotenv


ENV_NAMES = {
    'ACCESS_KEY': '',
    'ACCESS_KEY_SECRET': '',
    'CONSUMER_KEY': '',
    'CONSUMER_SECRET': '',
    'BEARER_TOKEN': '',
    'TEXT_PATH': 'data/agrippa.txt',

}


@pytest.fixture
def get_script_directory():
    directory = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    return directory


@pytest.fixture
def get_env_values(get_script_directory):
    root_dir = get_script_directory
    env_file = os.path.abspath(os.path.join(root_dir, '.env'))
    if os.path.isfile(env_file):
        load_dotenv()
        return dotenv.dotenv_values()
    else:
        values = {key: token for key, token in ENV_NAMES.items()}
        return values


@pytest.fixture
def get_text_path(get_script_directory, get_env_values):
    text_path = os.path.join(get_script_directory,
                             get_env_values['TEXT_PATH'])
    if os.path.isfile(text_path):
        abs_text_path = os.path.abspath(text_path)
    return abs_text_path
