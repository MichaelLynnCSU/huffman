import sys
import collections
import queue

def file_character_frequencies(file_name):
    # Suggested helper

    f = open(file_name)

    text = f.read()

 #   print(text)

    letters = collections.Counter(text)

    return letters


def treeTraversal(nodes, parent, ink, codeCount = ''):

    childs = nodes[parent]

    tree = {}

    if len(childs) == 2:

        tree['0'] = treeTraversal(nodes, childs[0], ink, codeCount + '0')

        tree['1'] = treeTraversal(nodes, childs[1], ink, codeCount + '1')

        return tree

    else:
        ink[parent] = codeCount

        return parent


def huffman_codes_from_frequencies(tuple):
    nodes = {}
    codes = {}

    for n in tuple.keys():
        nodes[n] = []

    freq = tuple.items()

    sorted_items = sorted(freq, key=lambda x:x[1])

    while len(tuple) > 1:
     #   print(sorted_items)

        item1 = sorted_items[0][0]

        item2 = sorted_items[1][0]

    #    print("here")
     #   print(a1)
     #   print(a2)
        tuple[item1+item2] = tuple.pop(item1) + tuple.pop(item2)

        freq = tuple.items()

        sorted_items = sorted(freq, key=lambda x:x[1]) # sort by second element in list

        newItem =  item1+item2

        nodes[newItem] = [item1, item2]

       # print(sorted_items)
         #print(nodes)

   # print(nodes)

    root = item1 + item2

 #   print("my root", root)

    code = {}

    treeTraversal(nodes, root, code)

    return code


def huffman_letter_codes_from_file_contents(file_name):
    """WE WILL GRADE BASED ON THIS FUNCTION."""
    # Suggested strategy...
    freqs = file_character_frequencies(file_name)
    return huffman_codes_from_frequencies(freqs)


def encode_file_using_codes(file_name, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name) as f:
        contents = f.read()
    file_name_encoded = file_name + "_encoded"
    with open(file_name_encoded, 'w') as fout:
        for c in contents:
            fout.write(letter_codes[c])
    print("Wrote encoded text to {}".format(file_name_encoded))


def decode_file_using_codes(file_name_encoded, letter_codes):
    """Provided to help you play with your code."""
    contents = ""
    with open(file_name_encoded) as f:
        contents = f.read()
    file_name_encoded_decoded = file_name_encoded + "_decoded"
    codes_to_letters = {v: k for k, v in letter_codes.items()}
    with open(file_name_encoded_decoded, 'w') as fout:
        num_decoded_chars = 0
        partial_code = ""
        while num_decoded_chars < len(contents):
            partial_code += contents[num_decoded_chars]
            num_decoded_chars += 1
            letter = codes_to_letters.get(partial_code)
            if letter:
                fout.write(letter)
                partial_code = ""
    print("Wrote decoded text to {}".format(file_name_encoded_decoded))


def main():
    """Provided to help you play with your code."""
    import pprint
    frequencies = file_character_frequencies(sys.argv[1])
    pprint.pprint(frequencies)
    codes = huffman_codes_from_frequencies(frequencies)
    pprint.pprint(codes)

   # codes = {'\n': '11010', ' ': '001', '!': '11100', ',': '11011', '.': '010',
     #        'd': '11001', 'e': '0001', 'g': '11101', 'h': '1111', 'l': '101', 'n': '11000', 'o': '100',
     #        'r': '0000', 'w': '001'}

  #  codes = {'\n': '11011', ' ': '101', '!': '0000', ',': '10101', '.': '011',
   #          'd': '11010', 'e': '11000', 'g': '0001', 'h': '1011', 'l': '100', 'n': '10100', 'o': '111',
    #         'r': '11001', 'w': '001'}


    encode_file_using_codes(sys.argv[1], codes)
    decode_file_using_codes("sentence1.txt_encoded",codes)
if __name__ == '__main__':
    """We are NOT grading you based on main, this is for you to play with."""
    main()
