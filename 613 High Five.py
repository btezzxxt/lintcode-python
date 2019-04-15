'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
from heapq import heappop, heappush
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        student = {}
        
        for record in results:
            if record.id not in student:
                student[record.id] = []
            heap = student[record.id]
            heappush(heap, record.score)
            if len(heap) > 5:
                heappop(heap)
        
        result = {}
        for id, heap in student.items():
            avg = 0
            length = len(heap)
            while heap:
                avg += heappop(heap)
            avg = avg / length
            result[id] = avg
        return result                
        