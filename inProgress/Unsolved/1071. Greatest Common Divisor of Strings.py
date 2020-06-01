def gcdOfStrings(str1, str2):
    gcd_string = ""
    gcd_values = []

    if len(str1)<= len(str2):
        for alpha in str1:
            gcd_string += alpha
            if gcd_string in str2:
                gcd_values.clear()
                gcd_values.append(gcd_string)
    else:
        for alpha in str2:
            gcd_string += alpha
            if gcd_string in str1:
                gcd_values.clear()
                gcd_values.append(gcd_string)

    return gcd_values


if __name__ == "__main__":
    # str1 = "ABCABC"
    # str2 = "ABC"
    str1 = "ABABAB"
    str2 = "ABAB"
    print(gcdOfStrings(str1, str2))