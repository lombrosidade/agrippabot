import os
import pytest
import dotenv
from dotenv import load_dotenv


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
    directory = get_script_directory
    env_file = os.path.abspath(os.path.join(directory, '.env'))
    load_dotenv(env_file)  # Load environment variables
    return dotenv.dotenv_values()


@pytest.fixture
def get_text_path(get_script_directory, get_env_values):
    text_path = os.path.join(get_script_directory,
                             get_env_values['TEXT_PATH'])
    abs_text_path = os.path.abspath(text_path)
    return abs_text_path
