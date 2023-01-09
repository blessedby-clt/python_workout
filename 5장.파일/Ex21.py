import os
def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

def find_all_longest(dirname):
    return {
        filename : find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname, filename))

    }

print(find_all_longest('./etc/'))