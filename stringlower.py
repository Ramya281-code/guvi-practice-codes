s=input().lower()
if any(ch in 'aeiou' for ch in s):
    print("yes")
else:
    print("no")