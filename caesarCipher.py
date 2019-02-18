

def caesarCipher(s, k):

    '''''
    cs = []
    for c in s:
        if
        print(ord(c))
        new_num = ord(c) + k
        cs.append(chr(new_num))
        print(cs)
    '''''
    for i in range(len(s)):

        if 97 <= ord(s[i]) <= 122:

            s = s[:i] + chr(((ord(s[i]) - 97 + k) % 26) + 97) + s[i + 1:]

        elif 65 <= ord(s[i]) <= 90:
            s = s[:i] + chr(((ord(s[i]) - 65 + k) % 26) + 65) + s[i + 1:]

    #print(s)







s = "ZZ-b-z"
k = 2

new_string = caesarCipher(s, k)


