class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for i in range(k):
            highestAmount = 0
            highestNum = 0

            for num, amount in count.items():
                if count[num] > highestAmount:
                    highestAmount = count[num]
                    highestNum = num

            output.append(highestNum)
            count[highestNum] = 0

        return output