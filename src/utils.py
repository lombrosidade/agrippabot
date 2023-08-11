from typing import List
import os
import re
import random


class FileReadError(Exception):
    """
    General exception class for handling file errors.
    """
    pass

def sanitize_line(line: str) -> str:
    """
    Sanitizes a line of text and ensures its word count is within limits.

    Args:
        line (str): The input line to sanitize.

    Returns:
        str: The sanitized line if it meets criteria, otherwise an empty string.
    """
    no_brackets = re.sub(r'\[.*?(\s|$|.*])', '', line.strip())
    no_space_before_punctuation = r'\s+([.,;!?:])\s*'
    line_sanitized = re.sub(no_space_before_punctuation, r'\1 ', no_brackets)
    line_sanitized = re.sub(r'\s+', ' ', line_sanitized)
    has_tweet_length = 3 <= len(line_sanitized) < 240
    starts_with_letter = re.match(r'^[a-zA-Z].*', line_sanitized)
    if has_tweet_length and starts_with_letter:
        return line_sanitized.strip()
    return ""


def read_lines(file_path: str) -> List[str]:
    """
    Reads lines from a text file, sanitizes them, and returns a list of valid lines.

    Args:
        file_path (str): The path to the text file to read.

    Returns:
        List[str]: A list of sanitized lines from the text file.
        
    Raises:
        FileReadError: If the file is not found or an error occurs while reading.
    """
    try:
        with open(file_path, 'r') as file:
            lines = []
            for paragraph in file:
                sentences = paragraph.split('.')
                for sentence in sentences:
                    if sanitize_line(sentence) != "":
                        lines.append(sentence)
            return lines
    except FileNotFoundError as exc:
        raise FileReadError("File not found: %s", exc)
    except Exception as general_exception:
        raise FileReadError("An error occurred: %s", generalexception)


def get_random_line(lines: List) -> str:
    """
    Returns a random line from a list of lines.

    Args:
        lines (List): A list of lines to choose from.

    Returns:
        str: A randomly selected line from the input list.
    """
    return random.choice(lines)

def get_script_directory() -> str:
    """
    Returns the absolute path of the script's directory.

    Returns:
        str: The absolute path of the script's directory.
    """
    directory = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    return directory

def get_text_file(dir, text_path):
    """
    Returns the absolute path of the text file within a directory.

    Args:
        dir (str): The directory containing the text file.
        text_path (str): The relative path to the text file.

    Returns:
        str: The absolute path of the text file.
    """
    text_path = os.path.join(dir,
                             text_path)
    abs_text_path = os.path.abspath(text_path)
    return abs_text_path