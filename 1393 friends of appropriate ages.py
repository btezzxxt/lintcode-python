import collections
class Solution:
    """
    @param ages: The ages
    @return: The answer
    """
    def numFriendRequests(self, ages):
        # Write your code here
        age_count = collections.defaultdict(int)
        for age in ages:
            age_count[age] += 1 
            
        count = 0
        for a in age_count.keys():
            for b in age_count.keys():
                if self.can_request(a, b):
                    if a == b:
                        count += age_count[a] * (age_count[b] - 1)
                    else:
                        count += age_count[a] * age_count[b]
        return count 
        
    def can_request(self, a, b):
        if b <= (0.5 * a + 7):
            return False 
        if b > a:
            return False
        if b > 100 and a < 100:
            return False 
        return True 
        
