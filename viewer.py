#!/usr/bin/env python3
"""
Python Code Viewer
-------------------
Terminal menu to browse and preview .py files stored in programs/.
Auto-detects files, no hardcoding. Syntax highlighting via pygments
if installed, else falls back to plain numbered lines.
"""

import os
import sys
import shutil

PROGRAMS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "programs")

try:
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import TerminalFormatter
    HAS_PYGMENTS = True
except ImportError:
    HAS_PYGMENTS = False


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def term_height():
    try:
        return shutil.get_terminal_size().lines
    except Exception:
        return 24


def print_banner():
    print("╔══════════════════════════════════════╗")
    print("║        PYTHON CODE VIEWER             ║")
    print("╚══════════════════════════════════════╝")
    print()


def get_python_files():
    if not os.path.isdir(PROGRAMS_DIR):
        return []
    files = [f for f in os.listdir(PROGRAMS_DIR) if f.endswith(".py")]
    return sorted(files)


def show_menu(files):
    clear_screen()
    print_banner()
    if not files:
        print("No .py files found in 'programs/' folder.")
        print("Add some Python files there and restart.\n")
        print("[Q] Quit")
        return
    print("Available Files:\n")
    for i, f in enumerate(files, start=1):
        print(f"[{i}] {f}")
    print("\n[Q] Quit")


def render_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        code = fh.read()

    if HAS_PYGMENTS:
        highlighted = highlight(code, PythonLexer(), TerminalFormatter())
        lines = highlighted.splitlines()
    else:
        lines = code.splitlines()

    numbered = []
    width = len(str(len(lines))) if lines else 1
    for i, line in enumerate(lines, start=1):
        numbered.append(f"{str(i).rjust(width)} | {line}")
    return numbered


def paginate(lines, filename):
    page_size = max(term_height() - 4, 5)
    total = len(lines)
    pos = 0

    while True:
        clear_screen()
        print(f"--- {filename} ---\n")
        chunk = lines[pos:pos + page_size]
        for line in chunk:
            print(line)

        remaining = total - (pos + page_size)
        print()
        if remaining > 0:
            print(f"[Enter] Next page   [B] Back to menu   ({remaining} lines left)")
        else:
            print("[End of file]   [B] Back to menu")

        choice = input("> ").strip().lower()
        if choice == "b":
            return
        elif remaining > 0:
            pos += page_size
        else:
            return


def main():
    if not os.path.isdir(PROGRAMS_DIR):
        os.makedirs(PROGRAMS_DIR, exist_ok=True)

    while True:
        files = get_python_files()
        show_menu(files)

        choice = input("\nSelect a file: ").strip().lower()

        if choice == "q":
            print("Goodbye.")
            sys.exit(0)

        if not files:
            input("\nPress Enter to refresh...")
            continue

        if not choice.isdigit():
            input("Invalid input. Press Enter to continue...")
            continue

        idx = int(choice)
        if idx < 1 or idx > len(files):
            input("Invalid selection. Press Enter to continue...")
            continue

        filename = files[idx - 1]
        filepath = os.path.join(PROGRAMS_DIR, filename)

        if not os.path.isfile(filepath):
            input("File no longer exists. Press Enter to continue...")
            continue

        try:
            lines = render_file(filepath)
            if not lines:
                clear_screen()
                print(f"--- {filename} ---\n\n(File is empty)\n")
                input("Press Enter to return to menu...")
            else:
                paginate(lines, filename)
        except Exception as e:
            input(f"Error reading file: {e}\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye.")
        sys.exit(0)