from os import terminal_size
from pathlib import Path
from typing import Text

def ls(path = Path.cwd()):
    return [f.name for f in path.glob("*")]

print(Path.cwd())
print(Path.home())

dpath = Path.cwd() / 'new_dir'
dpath.mkdir(exist_ok=True)
print(ls())
dpath.rmdir()
print(ls())

fpath = Path.cwd() / 'output.txt'
fpath.touch()
print(ls())
text = fpath.read_text()
print(text)
fpath.write_text('some text')
text = fpath.read_text()
print(text)
fpath.unlink()
print(ls())

