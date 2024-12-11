with open("input") as f:
    file_content = f.read()

drive = []

for i, x in enumerate(file_content):
    if i % 2 == 0:
        drive.append((int(x), i // 2))
    else:
        drive.append(int(x))

files = [f for f in drive if isinstance(f, tuple)][::-1]

for f in files:
    f_index = drive.index(f)
    print(f_index)
    for i, d in enumerate(drive[:f_index]):
        if isinstance(d, int):
            if d >= f[0]:
                drive[i] = d - f[0]
                drive.remove(f)
                drive.insert(f_index, f[0])
                drive.insert(i, f)

                break

hard_drive = []
for d in drive:
    if isinstance(d, int):
        hard_drive += [0] * d
    else:
        hard_drive += [d[1]] * d[0]
print(sum(i * k for i, k in enumerate(hard_drive)))
