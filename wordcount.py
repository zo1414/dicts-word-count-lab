# put your code here.


def word_counter(the_file):
    """Counts the times a word is in a file"""

    my_dict = {}
    input_file = open(the_file)

    for line in input_file:
        line = line.rstrip()
        for word in line.split(" "):
            word = word.rstrip(",")
            word = word.rstrip(".")
            word = word.rstrip("?")
            word = word.lower()
            my_dict[word] = my_dict.get(word, 0) + 1

    for k in my_dict.iteritems():
        print k[0], k[1]

#word_counter("test.txt")
word_counter("twain.txt")
