def is_palindrome(s: str) -> bool:
    """Return whether *s* reads the same forward and backward.

    Case and non-alphanumeric characters are ignored.
    """
    normalized = "".join(character.casefold() for character in s if character.isalnum())
    return normalized == normalized[::-1]


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in *text*."""
    return len(text.split())


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from degrees Celsius to degrees Fahrenheit."""
    return (celsius * 9 / 5) + 32