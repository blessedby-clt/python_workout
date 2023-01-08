def check_login(filename):
    users = {}

    with open(filename, 'r') as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                user_info = line.split(":")
                key = user_info[6].replace('\n', '')
                if key not in users.keys():
                    users[key] = []
                    
                users[key].append(user_info[0])


    return users

print(check_login('etc\passwd'))