names = ["henry spivey", "dk bhardwaj", "jatinder verma"]
print(names)
newNames = sorted(names, key=lambda name:name.split()[-1]) # O(n log n)
print(newNames)
