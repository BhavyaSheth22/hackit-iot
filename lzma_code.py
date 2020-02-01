import lzma
for i in range(50):

    original_data = open('./segregated_data/' + str(i) + '.txt', 'rb').read()
    compressed_data = lzma.compress(original_data)

    with open('./compressed_data/' + str(i) + '.txt', 'wb') as f:
        f.write(compressed_data)

    compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))
    print('Compressed: %d%%' % (100.0 * compress_ratio))