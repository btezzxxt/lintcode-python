import sys
class Solution:
    """
    @param tagList: The tag list.
    @param allTags: All the tags.
    @return: Return the answer
    """
    def getMinimumStringArray(self, tagList, allTags):
        # Write your code here
        contain = {}
        n = len(allTags)
        tag_list_map = set(tagList)
        
        l = 0
        r = 0
        
        res = sys.maxsize
        while r < n:
            while r < n and len(contain) < len(tagList):
                char = allTags[r]
                if char in tag_list_map:
                    count = contain.get(char, 0)
                    contain[char] = count + 1
                r += 1 
            
            if len(contain) < len(tagList):
                break
            
            while l < r:
                char = allTags[l]
                if char in tag_list_map:
                    count = contain[char]
                    contain[char] -= 1   
                    l += 1 
                    
                    if contain[char] == 0:
                        del contain[char]
                        res = min(res, r - l + 1)
                        break
                else:
                    l += 1
                
        return res if res != sys.maxsize else -1

print(Solution().getMinimumStringArray(["wrxqp","fygs","la","n","zw","ghk","lipf","vgzm","pe","yvoqu","fb","glf","pwa","ph","dmwpc","a","gbspu","lnw","oo","pvzur","cj","sjugp","c","vtrj","jy","vutvl","apsoc","t","g","tta","y","qqz","excku","tnuik","bpqna","bcwc","ljg","lw","bbon"], ["wrwky","yvoqu","tta","jmm","apsoc","tibt","cj","apsoc","c","bwgnv","wapz","yvoqu","pvzur","sl","oo","wrxqp","k","amq","excku","ucb","vutvl","nfw","c","bcwc","lnw","oh","linkq","zw","y","z","bb","npf","y","n","dsx","ghk","jy","w","zw","xyr","mpkod","gbspu","cj","ibg","xw","sjugp","qqz","gbspu","dmwpc","sjugp","apsoc","taikb","glf","n","ln","lv","n","t","ezzz","vlzx","lwn","vtrj","sjugp","vgzm","t","glf","rzrr","oo","pvzur","veio","pvzur","vutvl","lnw","fygs","ae","lnw","io","n","wrxqp","ph","ljg","pgmg","n","g","vl","ljg","lnw","tnuik","lw","zw","lw","rgn","oo","cj","tta","lnw","vutvl","y","oo","pwa","n","jtnoc","pwa","t","qiyh","v","bcwc","fb","vd","tta"]))