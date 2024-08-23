# lib/my_string.py

import re

class MyString:
    def __init__(self, value=''):
        self.value = value  # Use the setter to validate the initial value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return  # Exit the setter without changing the value
        self._value = new_value

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        if not self._value:
            return 0
        # Remove multiple punctuation marks to avoid counting them as multiple sentences
        cleaned_value = re.sub(r'[!?.]+', '.', self._value)
        # Split by period to separate sentences
        sentences = cleaned_value.split('.')
        # Filter out any empty strings that may occur due to consecutive periods
        non_empty_sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(non_empty_sentences)
