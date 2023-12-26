# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#### Python - Control Flow
### Decision-making Statements
# Decision making statements are used in the Python programs to make them able to decide which of the alternative group of instructions to be executed,
# depending on value of a certain Boolean expression.

## The if Statement
# Python provides if..elif..else control statements as a part of decision marking.
# Following is a simple example which makes use of if..elif..else. You can try to run this program using different marks and verify the result.
marks = 80 
result = ""
if marks < 30:
   result = "Failed"
elif marks > 75:
   result = "Passed with distinction"
else:
   result = "Passed"

print(result)

## The match Statement
def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))


### Loops or Iteration Statements
# Most of the processes require a group of instructions to be repeatedly executed. In programming terminology, it is called a loop.
# If the control goes back unconditionally, it forms an infinite loop which is not desired as the rest of the code would never get executed.
# In a conditional loop, the repeated iteration of block of statements goes on till a certain condition is met.

## The for Loop
words = ["one", "two", "three"]
for x in words:
  print(x)


## The while Loop
i = 1
while i < 6:
  print(i)
  i += 1
