from typing import List
import re
import random


# General exception for file handling errors
class FileReadError(Exception):
    pass

# Sanitizes each line and makes sure their word count is within limits


def sanitize_line(line: str) -> str:
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
    try:
        with open(file_path, 'r') as file:
            lines = []
            for paragraph in file:
                sentences = paragraph.split('.')
                for sentence in sentences:
                    if sanitize_line(sentence) != "":
                        lines.append(sentence)
            return lines
    except FileNotFoundError:
        raise FileReadError(f"File not found: {file_path}")
    except Exception as e:
        raise FileReadError(f"An error occurred: {e}")


def get_random_line(lines: List) -> str:
    return random.choice(lines)
