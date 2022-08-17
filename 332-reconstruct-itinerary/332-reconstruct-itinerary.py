class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = defaultdict(list)
        for item in tickets:
            dic[item[0]].append(item[1])
        
        path = ['JFK']
        def dfs(start):
            if len(path)==len(tickets)+1:
                return True
            dic[start].sort()
            for _ in dic[start]:
                end = dic[start].pop(0)
                path.append(end)
                if dfs(end):return True
                path.pop()
                dic[start].append(end)
                
        dfs('JFK')
        return path
        