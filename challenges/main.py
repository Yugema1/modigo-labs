def shared_hobbies(hobbies1, hobbies2):
    shared = set(hobbies1) & set(hobbies2)
    return shared
print(shared_hobbies(["reading", "chess"], ["chess", "cooking"]))