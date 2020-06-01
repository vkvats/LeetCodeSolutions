def canConstruct(ransomNote, magazine):
    mag = magazine
    for alpha in ransomNote:
        if alpha not in mag:
            return False
        elif alpha in magazine:
            mag = mag.replace(alpha, "_",1)
    return True

# best solution on leetcode
def canConstructBest(ransomNote, magazine):
    noteLetters = set(list(ransomNote))
    for l in noteLetters:
        if magazine.count(l) < ransomNote.count(l):
            return False

    return True

if __name__ == '__main__':
    ransomNote = "aab"
    magazine = "aab"
    print(canConstruct(ransomNote, magazine))