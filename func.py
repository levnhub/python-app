def test_func(word):
    print(word, end="")
    print("!")


test_func("Hi")
test_func(5)


def summa(a, b):
    res = a + b
    return res


res = summa(5, 7)
print(res)
print(summa("H", "i"))

# Minimal method

nums1 = [4, 7, 2, 1, 9]
nums2 = [4.4, 7.2, 2.1, 1.9, 9.5]


def minimal(nums):
    min_num = nums[0]
    for item in nums:
        if item < min_num:
            min_num = item

    print(min_num)
    # return min_num


minimal(nums1)
minimal(nums2)

# Anonym methods

func = lambda x, y: x * y

print(func(5, 2))
