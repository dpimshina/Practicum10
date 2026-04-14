def my_find(s, sub, start=0, end=None):
    if end is None:
        end = len(s)

    for i in range(start, end - len(sub) + 1):
        match = True

        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break

        if match:
            return i

    return -1

def find_all(s, sub):
    result = []

    for i in range(len(s) - len(sub) + 1):
        match = True

        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break

        if match:
            result.append(str(i))

    return ",".join(result)