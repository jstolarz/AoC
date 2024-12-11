with open("input") as f:
    file_content = f.read()

files_sizes = {}
break_sizes = {}
for i, x in enumerate(file_content):
    if i % 2 == 0:
        files_sizes[i // 2] = int(x)
    else:
        break_sizes[i // 2] = int(x)

breaks = list(break_sizes.items())
files = list(files_sizes.items())

pointer = 0

while True:
    pointer += 1
    f = files[-1]
    for b in breaks:
        if b[1] > 0:
            break
    else:
        print("end")
        break
    if b[1] >= f[1]:
        breaks[b[0]] = (b[0], b[1] - f[1])
        files = files[: b[0] + pointer] + [(f[0], f[1])] + files[b[0] + pointer : -1]
        breaks = breaks[:-1]
    else:  # f[1] > b[1]
        breaks[b[0]] = (b[0], 0)
        files = files[: b[0] + pointer] + [(f[0], b[1])] + files[b[0] + pointer :]
        files[-1] = (f[0], f[1] - b[1])
hard_drive = []
for f in files:
    hard_drive += [f[0]] * f[1]
print(sum(i * k for i, k in enumerate(hard_drive)))
