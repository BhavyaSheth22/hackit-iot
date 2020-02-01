import bz2
# from gen_json import make_block



original_data = open('block.txt', 'rb').read()
compressed_data = bz2.compress(original_data)

file1 = open('bz2_comp.txt', 'wb')
file1.write(compressed_data)
file1.close()

compress_ratio = (float(len(original_data)) -
                  float(len(compressed_data))) / float(len(original_data))
print('Compressed: %d%%' % (100.0 * compress_ratio))


# data = b'Welcome to TutorialsPoint'
# obj = lzma.LZMAFile("test.xz", mode="wb")
# obj.write(data)
# obj.close()

