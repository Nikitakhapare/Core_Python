'''
@Author: Nikita
@Date: 2022-04-04 18: 15: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-03 18: 15: 00
@Title:User Input and Replace String Template Hello <<UserName>>, How are you?
'''

oldstring="Hello <<userName>>, How are you"
userInput=input("Enter a new String ")
if len(userInput) < 3:
    print("Enter a proper user Name with more than 3 character")
else:
    newString=oldstring.replace("<<userName>>",userInput)
    print(newString)
  