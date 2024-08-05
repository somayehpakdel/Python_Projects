import math
import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk  # type: ignore


nltk.download('words')


class PasswordGenerator(ABC):

    def __init__(self) -> None:
        self.character_set: str = ''
        self.generated_password: str = ''

    @abstractmethod
    def generate_password(self) -> str:
        pass

    def calculate_entropy(self, password: Optional[str] = None) -> float:
        password = password or self.generated_password
        if password is None:
            raise ValueError("Password is not set")
        entropy: float = math.log2(len(self.character_set) ** len(password))
        print(f'Entropy : {entropy}')
        return entropy


class PinCodeGenerator(PasswordGenerator):
    """
    Generate a random numeric password.

    :param length: the length of the desired password
    :param character_set : set of possible characters
    """

    def __init__(self, length: int) -> None:
        super().__init__()
        self.length = length
        self.character_set = string.digits

    def generate_password(self) -> str:
        """
        Generate a random numeric password.

        :return: the generated password
        """
        self.generated_password = ''.join(random.choice(self.character_set) for _ in range(self.length))
        print(f'Passwod generated : {self.generated_password}')
        return self.generated_password


class RandomPasswordGenerator(PasswordGenerator):
    """
    Generate a random alphanumeric password.

    :param length: the length of the desired password
    :param character_set : set of possible characters
    """

    def __init__(
        self,
        length: int,
        include_numbers: Optional[bool] = None,
        include_symbols: Optional[bool] = None) -> None:
        super().__init__()
        self.length = length
        self.character_set = string.ascii_letters
        if include_numbers:
            self.character_set += string.digits
        if include_symbols:
            self.character_set += string.punctuation

    def generate_password(self) -> str:
        """
        Generate a random password contains alphabets , numbers, and symbols.

        :return: the generated password
        """
        self.generated_password = ''.join(random.choice(self.character_set) for _ in range(self.length))
        print(f'Passwod generated : {self.generated_password}')
        return self.generated_password


class MemorablePasswordGenerator(PasswordGenerator):

    def __init__(
        self,
        num_of_words: int,
        separator: str = '-',
        vocabulary: Optional[List[str]] = None) -> None:
        super().__init__()
        self.num_of_words = num_of_words 
        self.length: Optional[int] = None
        self.separator = separator
        self.vocabulary = vocabulary or nltk.corpus.words.words()
        self.character_set = string.ascii_letters + self.separator

    def generate_password(self) -> str:
        words = random.sample(self.vocabulary, self.num_of_words)
        self.generated_password = self.separator.join(words)
        self.length = len(self.generated_password)
        print(f'Passwod generated : {self.generated_password}')
        return self.generated_password


if __name__ == '__main__':
    pin_code_generator = PinCodeGenerator(6)
    pin_code_generator.generate_password()
    pin_code_generator.calculate_entropy()

    random_password_generator = RandomPasswordGenerator(12, include_numbers=True, include_symbols=True)
    random_password_generator.generate_password()
    random_password_generator.calculate_entropy()

    memorable_password_generator = MemorablePasswordGenerator(3)
    memorable_password_generator.generate_password()
    memorable_password_generator.calculate_entropy()