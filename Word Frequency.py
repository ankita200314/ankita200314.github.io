
fd = open("Example.txt", "r")
data = fd.read()
fd.close()

special_char = ",.?!"
for schar in special_char:
    if schar in data:
        data = data.replace(schar, "")

word_list = data.split()
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(f"{key} occurs : {value}")