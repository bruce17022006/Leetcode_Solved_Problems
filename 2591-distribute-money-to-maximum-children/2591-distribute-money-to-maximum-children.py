class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Rule 1: if not enough money to give at least $1 to each child → impossible
        if money < children:
            return -1

        # Step 1: Give $1 to each child
        remaining = money - children  

        # Step 2: Try to maximize children with $8
        count = min(children, remaining // 7)  

        # Step 3: Update remaining after giving 7 more to count children
        remaining -= count * 7
        left = children - count

        # Step 4: Handle tricky edge cases
        # Case A: All children got 8 but still money left → must reduce by 1
        if count == children and remaining > 0:
            count -= 1
        # Case B: One child is left, but leftover makes exactly 4 → reduce by 1
        elif count == children - 1 and remaining == 3:
            count -= 1

        return count
