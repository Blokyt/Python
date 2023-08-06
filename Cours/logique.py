def recursive(count):
    if count <= 0: # Condition d'arret
        return 0
    return 1 + recursive(count-1)

result = recursive(5)
print(result)
