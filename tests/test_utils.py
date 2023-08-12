from src.utils import sanitize_line, read_lines, get_random_line
import os
from .conftest import get_script_directory, get_env_values, get_text_path
import sys
import dotenv
from dotenv import load_dotenv
import pytest


@pytest.mark.parametrize("env_key",
                         [
                             "CONSUMER_KEY",
                             "CONSUMER_SECRET",
                             "ACCESS_KEY",
                             "ACCESS_KEY_SECRET",
                             "BEARER_TOKEN",
                             "TEXT_PATH"]
                         )
def test_env_has_all_values(get_env_values, env_key):
    env_values = get_env_values
    error_message = f"{env_key} is missing in the environment variables"
    assert env_key in env_values, error_message


def test_is_file(get_text_path):
    text_path = get_text_path
    assert os.path.isfile(text_path), "Text is not a file"


def test_reads_line(get_text_path):
    lines = read_lines(get_text_path)
    assert isinstance(lines, list), "read_lines should return a list"
    assert all(isinstance(line, str)
               for line in lines), "All lines should be strings"


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("Some [text]", "Some"),
        ("Some [text and another text]", "Some"),
        ("      ", ""),
        ("123", ""),
        ("[text", ""),
        ("e" * 2, ""),  # Minimum length threshold
        ("e" * 240, ""),  # Maximum length threshold
        # Add more test cases as needed
    ],
)
def test_sanitizes_line(input_text, expected_output):
    assert sanitize_line(input_text) == expected_output


def test_gets_random_line(get_text_path):
    lines = read_lines(get_text_path)
    random_line = get_random_line(lines)
    assert random_line in lines, "Random line should be one of the lines"
