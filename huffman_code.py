import HuffmanCoding

# input file path
path = "d:\iot\hackit-iot\zlib.txt"

h = HuffmanCoding(path)

output_path = h.compress()
h.decompress(output_path)
