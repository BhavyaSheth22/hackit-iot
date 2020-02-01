import random
import string

# file1 = open("text.txt", "a")

# for i in range(1000000):
#     file1.write(random.choice("ab"))

# file1.close()

with open("zlib.txt", 'w', encoding='utf-8') as f:
    for i in range(50000):
        f.write(random.choice("0123456789 abc"))
