from re import sub


def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


with open('types.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        className = line[4:].capitalize().replace(
            '\n', '').replace('\r', '')

        classSignature = f"""class {camel_case(className)}:\n\tpass"""
        with open('types.py', 'a') as f:
            f.write('\n' + classSignature)
