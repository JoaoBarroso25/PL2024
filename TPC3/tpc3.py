import re
import sys


def toggle_sum():
    collected_numbers = []
    total_sum = 0
    toggle = False

    for line in sys.stdin:
        found_items = re.findall(r'(on|off|=|\d)', line, re.IGNORECASE)
        collected_numbers.extend(found_items)

    for item in collected_numbers:
        if item.lower() == "on":
            toggle = True
        elif item.lower() == "off":
            toggle = False
        elif item.isdigit() and toggle:
            total_sum += int(item)
        elif item.lower() == "=":
            print("Somatório atual = ", total_sum)


def run_toggle_sum():
    toggle_sum()


if __name__ == "__main__":
    run_toggle_sum()
