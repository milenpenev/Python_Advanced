import os

dirpath, directories, files = next(os.walk(input()))

extensions = {}
for file in files:
    ext = file.split(".")[-1]
    if ext not in extensions:
        extensions[ext] = []
    extensions[ext].append(file)
with open(os.path.expanduser('~/Desktop/report.txt'), "w") as output_file:
    for ext in sorted(extensions.keys()):
        files = sorted(extensions[ext])
        output_file.write(f".{ext}\n")
        for file in files:
            output_file.write(f"---{file}\n")