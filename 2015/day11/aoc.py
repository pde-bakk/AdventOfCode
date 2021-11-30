def valid(pw: list) -> bool:
    check1 = False
    check2 = not any(c in ['i', 'o', 'l'] for c in pw)
    check3 = 0
    check3_letter = None
    for i, c in enumerate(pw):
        if i < len(pw) - 2:
            if ord(pw[i]) + 1 == ord(pw[i + 1]) and ord(pw[i + 1]) + 1 == ord(pw[i + 2]):
                check1 = True
        if i < len(pw) - 1 and pw[i] == pw[i + 1] and (pw[i] != check3_letter):
            check3_letter = pw[i]
            check3 += 1
        i += 1
    # print(f'{check1} and {check2} and {check3}')
    return check1 and check2 and check3 >= 2


def undo_confuse(pw: list) -> list:
    for i, c in enumerate(pw):
        if c in ['i', 'o', 'l']:
            pw[i] = chr(ord(pw[i]) + 1)
            for j in range(i + 1, len(pw)):
                pw[j] = 'a'
            break
    return pw


def increment(pw: list, i: int) -> list:
    if i < 0 or i >= len(pw):
        return pw
    if pw[i] == 'z':
        pw = increment(pw, i - 1)
        pw[i] = 'a'
    else:
        pw[i] = chr(ord(pw[i]) + 1)
    return pw


def part1(password: str) -> str:
    password = [c for c in password]
    i = len(password) - 1
    while not valid(password):
        password = increment(password, i)
        # print(password)
        password = undo_confuse(password)

    return ''.join(password)


def part2(pw: str) -> str:
    pw = [c for c in pw]
    pw = increment(pw, len(pw) - 1)
    return part1(''.join(pw))


print(part1('vzbxkghb'))
print(part2(part1('vzbxkghb')))
