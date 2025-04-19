def reformat(s):
    output = ""
    if len(s) ==1:
        return s
    if s.isalpha() and len(s)>=2:
        return output
    elif s.isnumeric() and len(s) >=2:
        return output
    else:
        string = []
        nums = []
        for value in s:
            if value.isalpha():
                string.append(value)
            else:
                nums.append(value)
    abs_diff = abs(len(nums) - len(string))
    if abs_diff > 1:
        return output
    if len(nums) > len(string):
        for index in range(len(nums)):
            if index + abs_diff !=len(nums):
                output += nums[index] + string[index]
            else:
                output += nums[index]
    elif len(string) > len(nums):
        for index in range(len(string)):
            if index + abs_diff != len(string):
                output += string[index] + nums[index]
            else:
                output += string[index]
    else:
        for index in range(len(string)):
            if index + abs_diff != len(string):
                output += string[index] + nums[index]
    return output

if __name__ == '__main__':
    s="3"
    # s = "leetcode"
    print(reformat(s))