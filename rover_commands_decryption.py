"""
Модуль для дешифрования команд для ровера.

Функции:
    - decrypt_command(encrypted_command: str) -> str:
        Дешифрует инструкцию в последовательность команд для ровера.
    - read_input() -> str:
        Считывает входные данные.
    - print_result(result: str) -> None:
        Выводит результат на консоль.
"""


# ID посылки: 123519155
def decrypt_command(encrypted_command: str) -> str:
    """
    Дешифруй строку команд для ровера.

    :param encrypted_command: Шифрованная инструкция.
    :return: Полная строка команд.
    """
    stack: list[tuple[int, str]] = []
    current_number: str = ''
    current_decryption: str = ''

    for character in encrypted_command:
        if '0' <= character <= '9':
            current_number += character
        elif character == '[':
            stack.append((int(current_number), current_decryption))
            current_number = ''
            current_decryption = ''
        elif character == ']':
            previous_number, previous_decryption = stack.pop()
            current_decryption = (
                previous_decryption
                + current_decryption * previous_number
            )
        else:
            current_decryption += character

    return current_decryption


def read_input() -> str:
    """
    Считай входные данные.

    :return: Строка с шифрованной инструкцией.
    """
    return input()


def print_result(result: str) -> None:
    """
    Выведи результат на консоль.

    :param result: Строка с дешифрованной инструкцией.
    :return: None
    """
    print(result)


if __name__ == '__main__':
    print_result(decrypt_command(read_input()))
