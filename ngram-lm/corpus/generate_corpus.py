import random
import itertools

silent_open = "<s> "
silent_close = " </s>"
lookup = ['BUKA', 'TUTUP', 'NYALAKAN', 'MATIKAN', 'HIDUPKAN', 'MAINKAN']
particle = ['DI']
object = ['PINTU', 'MUSIK', 'LAMPU', 'KIPAS', 'TV', 'TELEVISI', 'JENDELA']
location = ['KAMAR', 'DAPUR', 'TERAS', 'RUANG']
desc = ['TIDUR', 'MAKAN', 'KELUARGA', 'TAMU', 'DEPAN', 'BELAKANG']

l1 = [lookup, object, particle, location, desc]
l2 = [lookup, object]
l3 = [lookup, particle, object, location]
l4 = [lookup, object, location]
l5 = [lookup, object, location, desc]
lines_1 = [silent_open+"{} {} {} {} {}".format(*i)+silent_close for i in itertools.product(*l1)]
lines_2 = [silent_open+"{} {}".format(*i)+silent_close for i in itertools.product(*l2)]
lines_3 = [silent_open+"{} {} {} {}".format(*i)+silent_close for i in itertools.product(*l3)]
lines_4 = [silent_open+"{} {} {}".format(*i)+silent_close for i in itertools.product(*l4)]
lines_5 = [silent_open+"{} {} {} {}".format(*i)+silent_close for i in itertools.product(*l5)]
lines = lines_1 + lines_2 + lines_3 + lines_4 + lines_5
# for lup, part, obj, loc, des in zip(lookup, particle, object, location, desc):
#     line = F"- {lup} {obj} {part} {loc} {desc}"
#     lines.append(silent_open+line+silent_close)

# for lup, obj in zip(lookup, object):
#     line = F"- {lup} {obj}"
#     lines.append(silent_open+line+silent_close)

# for lup, part, obj, loc in zip(lookup, particle, object, location):
#     line = F"- {lup} {obj} {part} {loc}"
#     lines.append(silent_open+line+silent_close)

# for lup, obj, loc in zip(lookup, object, location):
#     line = F"- {lup} {obj} {loc}"
#     lines.append(silent_open+line+silent_close)

# for lup, obj, loc, des in zip(lookup, object, location, desc):
#     line = F"- {lup} {obj} {loc} {desc}"
#     lines.append(silent_open+line+silent_close)

random.shuffle(lines)
textfile = open("new_corpus.txt", "w")
for element in lines:
    textfile.write(element + "\n")
textfile.close()