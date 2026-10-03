# Python Code Viewer

Terminal menu tool. Browse `.py` files stored in `programs/`, pick one, view source with line numbers + syntax highlighting.

## Setup

```
git clone https://github.com/USERNAME/python-code-viewer.git
cd python-code-viewer
pip install -r requirements.txt
python viewer.py
```

## Usage

Drop `.py` files into `programs/`. Run `viewer.py`. Menu auto-lists them — no editing code needed.

```
╔══════════════════════════════════════╗
║        PYTHON CODE VIEWER             ║
╚══════════════════════════════════════╝

Available Files:

[1] program1.py
[2] program2.py
[3] program3.py

[Q] Quit

Select a file:
```

Enter number → view file, paged if long (`Enter` = next page, `B` = back to menu). `Q` quits anytime from menu.

## Notes

- No `pygments`? Falls back to plain numbered text, still works.
- Cross-platform: Linux, macOS, Windows (uses `cls`/`clear` automatically).
- No hardcoded filenames — add/remove files in `programs/` freely.