from collections import Counter
def get_count_aeiou(filename):
    with open(filename, 'r') as f:
        result = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for line in f:
            t = Counter(line)
            for key in t.keys():
                if key in result.keys():
                    result[key] = t[key]
            print(f'{line}:{result}')

def get_all_counter_aeiou(filename) :

    with open(filename, 'r') as f:
        for idx, line in enumerate(f):
            if idx == 0:
                counter = Counter(line)
            else:
                counter.update(line)

        print({key:value for key, value in counter.items() if key in 'aeiou'})

get_count_aeiou('etc/passwd')
get_all_counter_aeiou('etc/passwd')