## 내가 작성한 코드
def passwd_to_dict(filename):
    result = {}

    with open(filename, 'r') as f:
        for line in f:
            l = line.replace("\n", "").split(":")

            if len(l) >= 2:
                result[l[0]] = l[2]
    return result

## 책 코드
def passwd_to_dict(filename):
    users = {}
    with open(filename) as passwd:
        for line in passwd:
            if not line.startswith(("#", '\n')):
                user_info = line.split(":")
                users[user_info[0]] = int(user_info[2])
    return users

print(passwd_to_dict('etc/passwd'))