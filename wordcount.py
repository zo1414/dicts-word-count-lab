# put your code here.
from sys import argv


# def word_counter(the_file):
#     """Counts the times a word is in a file"""

#     my_dict = {}
#     input_file = open(the_file)

#     for line in input_file:
#         line = line.rstrip()
#         for word in line.split(" "):
#             word = word.strip(",:;'!.?_-")
#             word = word.strip('"')
#             word = word.rstrip(".")
#             word = word.rstrip("!")
#             word = word.lower()
#             my_dict[word] = my_dict.get(word, 0) + 1

#     for k in my_dict.iteritems():
#         print k[0], k[1]

#     return my_dict
# #word_counter("test.txt")
# text_file = argv[1]

# word_counter(text_file)

from collections import Counter

def word_counter(files):

    input_file = open(files).read().split()

    my_dict = Counter(input_file)

    return my_dict


wordcount = dict(word_counter('twain.txt'))
#print wordcount
print type(wordcount)
#print sorted(wordcount)
