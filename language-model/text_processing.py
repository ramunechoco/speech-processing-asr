import re

with open('tubes/wlist') as file:
    words_list = file.readlines()
    words_list = [line.rstrip() for line in words_list]
    words_list.pop(0)
pattern = re.compile('|'.join(r'\b{}\b'.format(word) for word in words_list))
print(words_list)
with open('lexicon/lexicon.txt', "r") as raw_data, \
        open('lexicon/indo_dict.txt', "w") as out:
        for line in raw_data:
            if pattern.search(line) != None:
                out.write(line)