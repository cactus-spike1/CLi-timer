#!/usr/bin/env python3
import time
import os
import sys
import argparse

# ASCII-арт представление цифр и двоеточия.
DIGITS = {
    "0": [
        " ┌───┐ ",
        " │   │ ",
        " │   │ ",
        " │   │ ",
        " └───┘ "
    ],
    "1": [
        "   ┌┐  ",
        "   ││  ",
        "   ││  ",
        "   ││  ",
        "   └┘  "
    ],
    "2": [
        " ┌───┐ ",
        "     │ ",
        " ┌───┘ ",
        " │     ",
        " └───┘ "
    ],
    "3": [
        " ┌───┐ ",
        "     │ ",
        " ┌───┤ ",
        "     │ ",
        " └───┘ "
    ],
    "4": [
        " │   │ ",
        " │   │ ",
        " └───┤ ",
        "     │ ",
        "     │ "
    ],
    "5": [
        " ┌───┐ ",
        " │     ",
        " └───┐ ",
        "     │ ",
        " └───┘ "
    ],
    "6": [
        " ┌───┐ ",
        " │     ",
        " ├───┐ ",
        " │   │ ",
        " └───┘ "
    ],
    "7": [
        " ┌───┐ ",
        "     │ ",
        "     │ ",
        "     │ ",
        "     │ "
    ],
    "8": [
        " ┌───┐ ",
        " │   │ ",
        " ├───┤ ",
        " │   │ ",
        " └───┘ "
    ],
    "9": [
        " ┌───┐ ",
        " │   │ ",
        " └───┤ ",
        "     │ ",
        " └───┘ "
    ],
    ":": [
        "   ",
        " ● ",
        "   ",
        " ● ",
        "   "
    ]
}

def clear_screen():
    """Очищает консоль в зависимости от операционной системы."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time_ascii(seconds):
    """
    Формирует время в формате HH:MM:SS (если часы > 0) или MM:SS и возвращает его ASCII-арт представление.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, sec = divmod(remainder, 60)

    if hours > 0:
        time_str = f"{hours:02d}:{minutes:02d}:{sec:02d}"
    else:
        time_str = f"{minutes:02d}:{sec:02d}"

    # Каждый символ превращаем в список строк.
    ascii_digits = [DIGITS[ch] for ch in time_str]

    # Объединяем построчно: для каждой строки (их 5) соединяем соответствующие строки каждого символа.
    result_lines = []
    for row in range(5):
        row_line = "   ".join(digit[row] for digit in ascii_digits)
        result_lines.append(row_line)

    return "\n".join(result_lines)

def run_timer(total_seconds, finished_msg, sound):
    try:
        for remaining in range(total_seconds, -1, -1):
            clear_screen()
            print("\033[32m" + format_time_ascii(remaining) + "\033[0m")
            time.sleep(1)
    except KeyboardInterrupt:
        clear_screen()
        print("Таймер прерван пользователем.")
        sys.exit(0)

    clear_screen()
    print("\033[35m " + finished_msg + " \033[0m")
    if sound:
        # ASCII BELL: может издать звуковой сигнал в терминале
        print("\a")  # спецсимвол BEL

def parse_args():
    parser = argparse.ArgumentParser(
        description="CLI таймера"
    )
    parser.add_argument(
        "seconds", type=int,
        help="Общее время таймера в секундах."
    )
    parser.add_argument(
        "-f", "--finished", type=str, default="Таймер завершён!",
        help="Сообщение после завершения отсчёта."
    )
    parser.add_argument(
        "--sound", action="store_true",
        help="Воспроизвести звуковой сигнал по завершении таймера."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    if args.seconds < 0:
        print("Время таймера не может быть отрицательным.")
        sys.exit(1)
    run_timer(args.seconds, args.finished, args.sound)

if __name__ == "__main__":
    main()
