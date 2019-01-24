"""
Details:
 Create a global variable called myUniqueList. It should be an empty list to start.
Next, create a function that allows you to add things to that list. 
Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList.
 If the value doesn't exist already, it should be added and the function should return True. 
 If the value does exist, it should not be added, and the function should return False;
Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers.
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""
#creating Global Variable 
myUniqueList = []
myLeftovers = []

#Giving Values from input
print("Add anything to The MyUniqueList :")
a = input(),input(),input(),input(),input()

#Adding values to the List
def var(a):
     myUniqueList.append(a[0])
     myUniqueList.append(a[1])
     myUniqueList.append(a[2])
     myUniqueList.append(a[3])
     myUniqueList.append(a[4])
var(a)
print("Added Values are :",myUniqueList)

v = input("\nEnter anything you have to pass:")
if v == myUniqueList[0] or v == myUniqueList[1] or v == myUniqueList[2] or v == myUniqueList[3] or v == myUniqueList[4]:
   print("\nFalse")
   myLeftovers.append(v)
   print("Value Exist Already")
   print("Added to MyLeftovers:",myLeftovers)
 
else:
   print("True")
   myUniqueList.append(v)
   print("\nValue Does not Exist,It should get added to myLeftovers")
   print("Added to MyUniqueList:",myUniqueList)
print("\n\nProgram Developed By: S Venkata Naveen")
