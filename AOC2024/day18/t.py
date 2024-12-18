FILE_NAME = "input"
READ_BYTES = 1024
SIZE = (70, 70)

with open(FILE_NAME) as f:
    lines = f.read().splitlines()
