import random
import string

file1 = open("text.txt", "a")

for i in range(1000000):
    file1.write(random.choice("ab"))

file1.close()
