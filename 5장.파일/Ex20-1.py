def target_word_count(filename, *words):
    result = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                if word in words:
                    result[word] = result.get(word, 0)
                    result[word] += 1
    return result

print(target_word_count('etc\wcfile.txt', 'words', 'contains', 'It'))



