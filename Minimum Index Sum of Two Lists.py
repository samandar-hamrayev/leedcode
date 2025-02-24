class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        map_list1 = {word: i for i, word in enumerate(list1)}
        min_index_sum = float('inf')
        res = []

        for idx, word in enumerate(list2):
            if word in map_list1:
                index_sum = map_list1[word] + idx
                if index_sum < min_index_sum:
                    min_index_sum = index_sum
                    res = [word]
                elif index_sum == min_index_sum:
                    res.append(word)

        return res

sol = Solution()
print(sol.findRestaurant(
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
))
