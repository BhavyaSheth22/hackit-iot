import lzma


def lzma_compress():
    original_data = open('block.txt', 'rb').read()
    print('==========\nCompressing...')
    compressed_data = lzma.compress(original_data)

    with open('comp_block.txt', 'wb') as f:
        f.write(compressed_data)

    compress_ratio = (float(len(original_data)) -
                      float(len(compressed_data))) / float(len(original_data))
    print('Compressed: %d%%' % (100.0 * compress_ratio), '==========')
