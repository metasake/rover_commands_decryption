"""
Модуль для дешифрования команд для ровера.

Функции:
    - decrypt_command(encrypted_command: str) -> str:
        Дешифрует строку команд для ровера.
    - read_input() -> str:
        Считывает входные данные.
    - print_result(result: str) -> None:
        Выводит результат на консоль.
"""


# ID посылки: 123451531
def decrypt_command(encrypted_command: str) -> str:
    """
    Дешифруй строку команд для ровера.

    :param encrypted_command: Сжатая строка команд.
    :return: Полная строка команд.
    """
    stack: list[tuple[int, str]] = []
    current_number: int = 0
    current_string: str = ''

    for character in encrypted_command:
        if character.isdigit():
            current_number = current_number * 10 + int(character)
        elif character == '[':
            stack.append((current_number, current_string))
            current_number = 0
            current_string = ''
        elif character == ']':
            previous_number, previous_string = stack.pop()
            current_string = previous_string + current_string * previous_number
        else:
            current_string += character

    return current_string


def read_input() -> str:
    """
    Считай входные данные.

    :return: Строка с шифрованной инструкцией.
    """
    encrypted_command: str = input()
    return encrypted_command


def print_result(result: str) -> None:
    """
    Выведи результат на консоль.

    :param result: Строка с дешифрованной инструкцией.
    :return: None
    """
    print(result)


if __name__ == '__main__':
    encrypted_command: str = read_input()
    print_result(decrypt_command(encrypted_command))
