# Naive solution
def decompressRLElist(nums):
    length = len(nums)
    decompressed = []

    assert (length % 2 == 0)
    #     assert(length>=2 and length <=100)

    for i in range(0, length, 2):
        frequnecy = nums[i]
        value = nums[i + 1]
        for j in range(frequnecy):
            decompressed.append(value)
    return decompressed


# list multiplication
def decompressRLElistLM(nums):
    length = len(nums)
    decompressed = []
    for i in range(0, length, 2):
        temp = []
        freq = nums[i]
        val = nums[i + 1]
        temp.append(val)
        temp = temp * freq
        decompressed.extend(temp)
    return decompressed


import time
import numpy as np

# nums = np.arange(10000)
nums = [1, 1, 2, 3]
t1 = time.time()
decompressRLElist(nums)
t2 = time.time()
print(decompressRLElistLM(nums))
t3 = time.time()
print(f"Method 1 took {t1 - t2} time")
print(f"Method 2 took {t2 - t3} time")