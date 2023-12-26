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
from IPython.display import Image

#### Python if-else Statement
### Python − if-else Statement
# Along with the if statement, else keyword can also be optionally used.
# It provides an alternate block of statements to be executed if the Boolean expression (in if statement) is not true.
# this flowchart shows how else block is used.
Image("https://www.tutorialspoint.com/python/images/ifelse_syntax.jpg")

# +
## Syntax
# Python implementation of the above flowchart is as follows −
# if expr==True:
#    stmt1
#    stmt2
#    stmt3
# else:
#    stmt4
#    stmt5
#    stmt6
# Stmt7

Image("https://www.tutorialspoint.com/python/images/ifelse.jpg")
# -

# age=25
age=17
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")

# +
### Python − elif Statement
# The elif statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.
# Similar to the else statement, the elif statement is optional. However, unlike else, for which there can be at the most one statement;
# there can be an arbitrary number of elif statements following an if.

## Syntax
# if expression1:
#    statement(s)
# elif expression2:
#    statement(s)
# elif expression3:
#    statement(s)
# else:
#    statement(s)

## Example
Image("https://www.tutorialspoint.com/python/images/ifelif.jpg")

# +
# amount = 2500
amount = 12000
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
else:
   if amount > 5000:
      discount = amount * 10 / 100
   else:
      if amount > 1000:
         discount = amount * 5 / 100
      else:
         discount = 0

print('Payable amount = ',amount - discount)

# +
# While the code will work perfectly ok, if you look at the increasing level of indentation at each if and else statement,
# it will become difficult to manage if there are still more conditions.

# The elif statement makes the code easy to read and comprehend.

# Elif is short for else if. It allows the logic to be arranged in a cascade of elif statements after the first if statement.
# If the first if statement evaluates to false, subsequent elif statements are evaluated one by one and comes out of the cascade if any one is satisfied.
# Last in the cascade is the else block which will come in picture when all preceding if/elif conditions fail.

amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

# +
### Python - Nested If Statements
# There may be a situation when you want to check for another condition after a condition resolves to true.
# In such a situation, you can use the nested if construct.
# In a nested if construct, you can have an if...elif...else construct inside another if...elif...else construct.

## Syntax
# The syntax of the nested if...elif...else construct will be like this −
# if expression1:
#    statement(s)
#    if expression2:
#       statement(s)
#    elif expression3:
#       statement(s)3
#    else
#       statement(s)
# elif expression4:
#    statement(s)
# else:
#    statement(s)

## Example
num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")
