# Python Error Cheatsheet

## Error 1: IndexError

**What it means:** You're trying to access an index that doesn't exist in a list.

**Common causes:**
- Index is out of range
- Negative index too large
- Empty list

**Code that triggers it:**
```python
lst = [1, 2, 3]
print(lst[5])  # IndexError: list index out of range
```

**Code that fixes it:**
```python
lst = [1, 2, 3]
if len(lst) > 5:
    print(lst[5])
else:
    print("Index out of range")

# OR check length first
index = 5
if 0 <= index < len(lst):
    print(lst[index])
```

---

## Error 2: KeyError

**What it means:** You're trying to access a dictionary key that doesn't exist.

**Common causes:**
- Key name is wrong
- Key hasn't been added yet
- Case sensitivity mismatch

**Code that triggers it:**
```python
data = {"name": "Virat", "age": 20}
print(data["city"])  # KeyError: 'city'
```

**Code that fixes it:**
```python
data = {"name": "Virat", "age": 20}

# Option 1: Check if key exists
if "city" in data:
    print(data["city"])
else:
    print("Key not found")

# Option 2: Use get() method
print(data.get("city", "Not found"))  # Returns "Not found" if key doesn't exist
```

---

## Error 3: TypeError

**What it means:** You're performing an operation on incompatible data types.

**Common causes:**
- Concatenating string + integer
- Calling a non-callable object
- Wrong argument type for function

**Code that triggers it:**
```python
name = "Virat"
age = 20
print("My name is " + name + " and I'm " + age + " years old")
# TypeError: can only concatenate str (not "int") to str
```

**Code that fixes it:**
```python
name = "Virat"
age = 20

# Option 1: Convert to string
print("My name is " + name + " and I'm " + str(age) + " years old")

# Option 2: Use f-string (better)
print(f"My name is {name} and I'm {age} years old")

# Option 3: Use format()
print("My name is {} and I'm {} years old".format(name, age))
```

---

## Error 4: RecursionError

**What it means:** A function calls itself infinitely (no base case to stop).

**Common causes:**
- Missing or incorrect base case
- Base case never reached
- Wrong termination condition

**Code that triggers it:**
```python
def countdown(n):
    print(n)
    countdown(n - 1)  # Never stops!

countdown(5)
# RecursionError: maximum recursion depth exceeded
```

**Code that fixes it:**
```python
def countdown(n):
    if n <= 0:  # BASE CASE - when to stop
        print("Done!")
        return
    print(n)
    countdown(n - 1)  # Recursive call

countdown(5)  # Prints 5, 4, 3, 2, 1, Done!
```

---

## Error 5: AttributeError

**What it means:** An object doesn't have the attribute/method you're trying to access.

**Common causes:**
- Typo in method name
- Method doesn't exist for that object type
- Accessing attribute before it's defined

**Code that triggers it:**
```python
name = "Virat"
print(name.append("x"))  # AttributeError: 'str' object has no attribute 'append'
# (append() is for lists, not strings)
```

**Code that fixes it:**
```python
# Option 1: Use correct method for string
name = "Virat"
name_list = list(name)
name_list.append("x")
print(name_list)  # ['V', 'i', 'r', 'a', 't', 'x']

# Option 2: Check if object has attribute
name = "Virat"
if hasattr(name, 'append'):
    name.append("x")
else:
    print("String doesn't have append method")

# Option 3: Use try-except
try:
    name.append("x")
except AttributeError:
    print("Method doesn't exist")
```

---

## Quick Reference

| Error | Cause | Quick Fix |
|-------|-------|-----------|
| IndexError | Index out of range | Check `len()` before accessing |
| KeyError | Dictionary key doesn't exist | Use `.get()` or check `if key in dict` |
| TypeError | Wrong data types | Convert types or use f-strings |
| RecursionError | Infinite recursion | Add base case to stop recursion |
| AttributeError | Object has no attribute | Check method exists or use `hasattr()` |