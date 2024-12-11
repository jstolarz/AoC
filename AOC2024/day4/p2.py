with open("input") as f:
    word_search = f.readlines()


target_word = "MAS"
target_word_length = len(target_word)
count = 0
n = len(word_search)
m = len(word_search[0])


for i in range(1, n - 1):
    for j in range(1, m - 1):
        la = "".join([word_search[i + k][j + k] for k in range(-1, 2)])
        ra = "".join([word_search[i + k][j - k] for k in range(-1, 2)])
        if (la == target_word or la[::-1] == target_word) and (
            ra == target_word or ra[::-1] == target_word
        ):
            count += 1
print(count)
