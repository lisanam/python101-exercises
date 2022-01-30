# combine .md files in notes to create one giant notes called notes
import glob
import fileinput
import pathlib

file_path = str(pathlib.Path().joinpath('notes/*.md').resolve())

with open('notes.md', 'w') as file_out:
    file_out.write("#Hi")
    files = glob.glob(file_path)

    for line in sorted(fileinput.input(files)):
        file_out.write(line)