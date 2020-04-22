class sumValues:
    def sumList(self):
        # Python program to sum elements in  a list 
        input_string = input("Enter a list numbers or elements separated by space: ")
        aList = input_string.split()

        # Convert string list to integer list to allow integer operand
        aList = [int(i) for i in aList] 
        print("List with values as integer is: ", aList)

        # using sum() function 
        total = sum(aList) 
  
        # printing total value 
        print("Sum of All list values =", total)
        return total

class assignsumValues:
    def assigntoString(self):
        listsumstr = sumValues.sumList(self)
        
        print(str(listsumstr))
        return str(listsumstr)
        

value2get = assignsumValues()
test1 = value2get.assigntoString()

print('this is string: ' + test1)
