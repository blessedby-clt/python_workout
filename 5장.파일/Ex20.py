def wc(filename):
    counts = {'characters':0, 'words':0, 'lines':0}
    unique_counts = set()
    with open(filename, 'r') as f:
        for line in f:
            counts['characters'] += len(line)
            counts['words']+= len(line.split())
            counts['lines']+= 1
            unique_counts.update(line.split())
    counts['unique words'] = len(unique_counts)
    return counts

print(wc('etc/wcfile.txt'))