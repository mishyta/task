from pathlib import Path

def ls(path = Path.cwd()): # how ls in linux
    return [f.name for f in path.glob("*")] # List comprehension "the contents of the folder"

print(Path.cwd()) # displays the path to the current dir
print(Path.home()) # displays the path to home

dpath = Path.cwd() / 'new_dir' # create dpath with path 'current dir/new_dir
print(dpath)
dpath.mkdir(exist_ok=True) # create dir 'new_dir' in current dir
print(ls())
dpath.rmdir() # remove dir 'new_dir' in current dir
print(ls())

fpath = Path.cwd() / 'output.txt' # create dpath with path 'current dir/output.txt
print(fpath)
fpath.touch()  # create file 'new_dir' in current dir
print(ls())
text = fpath.read_text() # read file
print(text)
fpath.write_text('some text') # write to file
text = fpath.read_text()
print(text)
fpath.unlink() # delete file
print(ls())

