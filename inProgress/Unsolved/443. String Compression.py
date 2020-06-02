def compress(chars):
    result = ""
    count = {}
    for alpha in chars:
        count[alpha] = count.get(alpha,0) + 1
    for key, value in count.items():
        if value ==1:
            result += key
        else:
            result += key + str(value)
    return len(result) # list(result)

def compressInplace(chars):
    visited = []
    new_chars = chars[:]
    for index, alpha in enumerate(new_chars):
        if alpha not in visited:
            chars.insert(index+1, chars.count(alpha))
            visited.append(alpha)
        else:
            chars.pop(index)
    return chars

if __name__ == '__main__':
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"] # ["a","b","1","2"].
    charsj = ["a","a","a","b","b","a","a"]
    print(compressInplace(chars))