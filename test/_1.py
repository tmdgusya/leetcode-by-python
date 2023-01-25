import unittest


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        expected = [0, 1]
        self.assertEqual(self.twoSum([2, 7, 11, 15], 9), expected)

    def test_case_2(self):
        nums = [3, 2, 4]
        expected = [1, 2]
        self.assertEqual(self.twoSum(nums, 6), expected)

    def test_case_3(self):
        nums = [3, 3]
        expected = [0, 1]
        self.assertEqual(self.twoSum(nums, 6), expected)

    def test_case_4(self):
        nums = [-1,-2,-3,-4,-5]
        expected = [2, 4]
        self.assertEqual(self.twoSum(nums, -8), expected)

    def twoSum(self, nums, target):
        cache = {}
        for idx, num in enumerate(nums):
            cache[num] = idx
        for idx, num in enumerate(nums):
            if target - num in cache and cache[target - num] != idx:
                return [idx, cache[target - num]]
        return []


    def twoSumBySquare(self, nums, target):
        for idx, num in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx == idx2:
                    continue
                if target == num + num2:
                    return [idx, idx2]

        return []





if __name__ == '__main__':
    unittest.main()
