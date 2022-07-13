"""
Baseball Game

You are keeping score for a baseball game with strange rules. The game consists of several rounds, 
where the scores of past rounds may affect future rounds' scores
At the beginning of the game, you start with an empty record You are given a list of strings ops, 
where ops[i] is the ith operation you must apply to the record and is one of the following: 
0. An integer x - Record a new score of x 
0. "+" - Record a new score that is the sum of the previous two scores. 
It is guaranteed there will always be two previous 
0. "D" - Record a new score that is double the previous score. 
It is guaranteed there will always be a previous score. 
0. "C" Invalidate the previous score, removing it from the record. 
It is guaranteed there will always be a previous score

Example 1:
Input: ops ["5","2","c","D","+"] 
Output: 30
Explanation: 
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15).
The total sun is 5 + 10 + 15 = 30.

Example 2:
Inputs ops = ["5"."-2","4","C","D","9","+","+"]
Output: 27 Explanation:
"5" - Add to the record, record is now [5].
"-2" - Add to the record, record is now [5, -2].
"4" - Add to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Record a new score that is double the previous score. Record is now [5, -2, -4]
"9" - Add to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5]
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14]
The total sum is 5 + (-2) + (-4) + 9 + 5 + 14 = 27 
"""

def calPoints(ops) -> int:
    """
    :type ops: List[str] - List of operations
    :rtype: int - Sum of scores after performing all operations
    """
    sumList1 = 0
    i=0
    list1 = []
    
    for item in ops:
        #Starts with letters to prevent int transformation error
        if item == "C":
            list1.pop()
        elif item == "D":
            doubleItem = 2*int(list1[i-1])
            list1.append(doubleItem)
        elif item == "+":
            if len(list1) >= 2:
                print(i)
                sumItems = int(list1[i-2])+int(list1[i-1])
                list1.append(sumItems)
            if len(list1) < 2:
                list1.append(list1[i])
        elif int(item):
            list1.append(item)
        #Increment for control list vector        
        i=len(list1)
        print(list1)
    
    for item2 in list1:
        sumList1 = sumList1 + int(item2)
        
    result = sumList1
    return result

if __name__=='__main__':
    line = input()
    ops = line.strip().split()

    print(calPoints(ops))