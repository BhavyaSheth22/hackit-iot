import lzma
import json

original_data = open('comp_block.txt', 'rb').read()



og_block = lzma.decompress(original_data)
# print(og_block[:20])
og_block = json.loads(og_block.decode('utf-8'))

print(og_block)
with open("og_data.txt", 'wb') as f:
    f.write(og_block)
