import zlib

original_data = open('zlib.txt', 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)

compress_ratio = (float(len(original_data)) -
                  float(len(compressed_data))) / float(len(original_data))

file1 = open('zlib_comp.txt', 'wb')
file1.write(compressed_data)
file1.close()

print(type(compressed_data))
print('Compressed: %d%%' % (100.0 * compress_ratio))
