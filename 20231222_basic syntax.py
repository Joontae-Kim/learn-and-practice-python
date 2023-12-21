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
# Python Syntax
# Summary
# A Python statement ends with a newline character. (개행문자로 끝납니다.)
# Python uses spaces and indentation to organize its code structure. (Python은 공백과 들여쓰기를 사용하여 코드 구조를 구성합니다.)
# Identifiers are names that identify variables, functions, modules, classes, etc. in Python. (식별자는 Python에서 변수, 함수, 모듈, 클래스 등을 식별하는 이름입니다.)
# Comments describe why the code works. They are ignored by the Python interpreter.(주석은 코드가 작동하는 이유를 설명합니다. Python 인터프리터에서는 무시됩니다.)
# Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote (작은 따옴표, 큰 따옴표, 삼중 따옴표 또는 삼중 큰 따옴표를 사용하여 표시하십시오.)


### 1. Whitespace and indentation
## Python uses whitespace and indentation to construct the code structure.

# example) define main function to print out something
# 각 줄의 끝에는 명령문을 종료하는 세미콜론이 표시되지 않습니다. 그리고 코드는 들여쓰기를 사용하여 코드 형식을 지정합니다.
# 들여쓰기와 공백을 사용하여 코드를 구성하면 Python 코드는 다음과 같은 이점을 얻습니다.
# # 첫째, Java나 C#과 같은 다른 프로그래밍 언어처럼 블록의 시작 또는 끝 코드를 놓치지 않습니다.
# # 둘째, 코딩 스타일이 본질적으로 균일합니다. 다른 개발자의 코드를 유지해야 한다면 해당 코드는 귀하의 코드와 동일해 보입니다.
# # 셋째, 코드는 다른 프로그래밍 언어에 비해 읽기 쉽고 명확합니다
# # 
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()

### 2. Comments
# 주석은 코드가 작성된 이유를 설명하므로 코드만큼 중요합니다.
# Python 인터프리터는 코드를 실행할 때 주석을 무시합니다.
# Python에서 한 줄 주석은 해시(#) 기호로 시작하고 그 뒤에 주석이 옵니다.

# 1) One-line docstrings
# 한 줄 독스트링은 삼중따옴표(""")로 시작하고 삼중따옴표(""")로 끝납니다. 또한 한 줄 독스트링 앞이나 뒤에 빈 줄이 없습니다.
# def quicksort():
# """ sort the list using quicksort algorithm """
# ...

# 2) Multi-line docstrings
# 여러 줄로 된 독스트링은 삼중따옴표(""")로 시작하고 삼중따옴표(""")로 끝납니다.
# 예제 1)
# def increase(salary, percentage, rating):
#    """ increase salary base on rating and percentage
#   rating 1 - 2 no increase
#   rating 3 - 4 increase 5%
#   rating 4 - 6 increase 10%
#   """

# 예제2)
# [], {} 또는 () 대괄호 안에 포함된 명령문에서는 줄 연속 문자를 사용할 필요가 없습니다. 예를 들어 다음 명령문은 Python에서 잘 작동합니다.
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

### 3. Continuation of statements (진술의 계속)
# Python은 개행 문자를 사용하여 명령문을 구분합니다. 각 명령문을 한 줄에 배치합니다.
# 그러나 긴 문은 백슬래시(\) 문자를 사용하여 여러 줄에 걸쳐 있을 수 있습니다.
a = False
b = False
C = False # True, False
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")


### 4. Identifiers (식별자)
# 식별자는 Python에서 변수, 함수, 모듈, 클래스 및 기타 개체를 식별하는 이름입니다.
# 식별자 이름은 문자나 밑줄(_)로 시작해야 합니다. 다음 문자는 영숫자 또는 밑줄일 수 있습니다.
# Python 식별자는 대소문자를 구분합니다. 예를 들어 `counter` and `Counter` 서로 다른 식별자입니다.
# 또한 식별자 이름을 지정하는 데 Python 키워드를 사용할 수 없습니다.


### 5. Keywords
# 일부 단어는 Python에서 특별한 의미를 갖습니다. 이를 키워드라고 합니다.
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# Python은 키워드라는 키워드를 나열하기 위한 특수 모듈을 제공합니다.


### 6. String literals
# Python에서는 작은따옴표('), 큰따옴표("), 세 개의 작은따옴표(''') 및 세 개의 큰따옴표(""")를 사용하여 문자열 리터럴을 나타냅니다.
# 문자열 리터럴은 동일한 유형의 따옴표로 묶어야 합니다. 예를 들어 작은따옴표를 사용하여 문자열 리터럴을 시작하는 경우 동일한 작은따옴표를 사용하여 문자열 리터럴을 끝내야 합니다.
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)

# -


