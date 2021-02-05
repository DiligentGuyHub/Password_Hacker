# the list "meals" is already defined
# your code here
result = 0
for x in meals:
    result += x.get("kcal")
print(result)
