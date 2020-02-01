import lzma

original_data = open('zlib.txt', 'rb').read()
compressed_data = lzma.compress(original_data)

file1 = open('lzma_comp.txt', 'wb')
file1.write(compressed_data)
file1.close()

compress_ratio = (float(len(original_data)) -
                  float(len(compressed_data))) / float(len(original_data))
print('Compressed: %d%%' % (100.0 * compress_ratio))


# data = b'Welcome to TutorialsPoint'
# obj = lzma.LZMAFile("test.xz", mode="wb")
# obj.write(data)
# obj.close()
