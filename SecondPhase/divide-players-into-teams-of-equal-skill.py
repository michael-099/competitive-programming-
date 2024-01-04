class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right, res = 0, len(skill) - 1, 0
        var = skill[left] + skill[right]

        while left <= right:
            if skill[left] + skill[right] != var:
                return -1
            else:
                res = res + (skill[left] * skill[right])
                right -= 1
                left += 1
        return res
