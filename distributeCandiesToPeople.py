class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        toGive = 1
        holder = num_people
        ppl = [0]*num_people
        while candies != 0:
            if candies < toGive:
                ppl[holder%num_people] += candies
                return ppl
            else:
                ppl[holder%num_people] += toGive
                candies -= toGive
                toGive += 1 
                holder += 1
        return ppl
