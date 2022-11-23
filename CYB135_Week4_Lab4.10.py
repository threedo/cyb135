#CYB135 Week4 Lab 4.10
'''
4.10 LAB: All permutations of names
Write a program that lists all ways people can line up for a photo (all permutations of a list of strings). The program will read a list of one word names, then use a recursive method to create and output all possible orderings of those names, one ordering per line.

When the input is:

Julia Lucas Mia
then the output is (must match the below ordering):

Julia Lucas Mia
Julia Mia Lucas
Lucas Julia Mia
Lucas Mia Julia
Mia Julia Lucas
Mia Lucas Julia
'''

def all_permutations(permList, nameList):
   def create_Permutations(nameList):
       q = len(nameList)
       if q == 0:
           return []
       if q == 1:
           return [nameList]
       permList = []
       for i in range(q):
           w = nameList[i]
           e = nameList[:i] + nameList[i+1:]
           for r in create_Permutations(e):
               permList.append([w] + r)
       return permList
   permList = create_Permutations(nameList)
   for r in permList:
       for t in r:
           print(t, end = " ")
       print()


if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)
