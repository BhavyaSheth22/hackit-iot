import lzma

original_data = open('comp_block.txt', 'rb').read()

og_block = lzma.decompress(original_data)
with open("og_data.txt", 'wb') as f:
    f.write(og_block)
