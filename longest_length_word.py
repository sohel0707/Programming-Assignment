string = input()
words = string.split()

max_len = 0
max_len_word = ""
for i in words:
    cur_len = len(i)
    if max_len < cur_len:
        max_len = cur_len
        max_len_word = i
print(max_len_word)
