---
title: "unit-tests-labs"
type: "lab"
---
def age_calculator(current_year, birth_year):
  # Returns the age of a person
  age = current_year - birth_year
  if age < 0: # If age is not a positive number, do not return the age
    print("Not a correct age!")
  else:
    return age

if __name__ == '__main__':
  print(age_calculator(2018, 1995))
```
Write a test validating that the function we wrote will always return a positive number for age.