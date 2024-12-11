with open("input") as f:
    word_search = f.readlines()

target_word = "XMAS"
target_word_length = len(target_word)
count = 0
n = len(word_search)
m = len(word_search[0])

for i in range(n):
    for j in range(m):
        if j + target_word_length <= m:
            search = word_search[i][j : j + target_word_length]
            if search == target_word or search[::-1] == target_word:
                count += 1
                print(i, j, search, "1")
        if i + target_word_length <= n:
            search = "".join([word_search[i + k][j] for k in range(target_word_length)])
            if search == target_word or search[::-1] == target_word:
                count += 1
                print(i, j, search, "2")
        if i + target_word_length <= n and j + target_word_length <= m:
            search = "".join(
                [word_search[i + k][j + k] for k in range(target_word_length)]
            )
            if search == target_word or search[::-1] == target_word:
                count += 1
                print(i, j, search, "3")
        if i + target_word_length <= n and j - target_word_length + 1 >= 0:
            search = "".join(
                [word_search[i + k][j - k] for k in range(target_word_length)]
            )
            if search == target_word or search[::-1] == target_word:
                count += 1
                print(i, j, search, "4")
print(count)
