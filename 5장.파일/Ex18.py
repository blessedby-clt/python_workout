def get_final_line(filename):
    final_line = ''
    with open(filename, 'r') as f:
        for line in f:
            final_line = line
    return final_line

print(get_final_line('etc/passwd'))