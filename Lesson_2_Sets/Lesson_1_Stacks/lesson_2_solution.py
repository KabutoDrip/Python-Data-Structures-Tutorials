person1 = {0,2,4,6,8,10,12,14,16,18,20}
person2 = {1,3,5,7,9,11,13,15,17,19,21}
person3 = {0,2,5,7,9,11,13,15,16,19,20}
person4 = {0,2,5,7,8,10,12,14,17,18,21}
person5 = {0,3,4,6,9,11,12,14,17,19,21}
person6 = {1,3,4,6,9,10,12,15,16,18,21}

#Begin problem 1
def evaluate(p1):
    evens = 0
    for item in p1:
        if (item % 2 == 0):
            evens += 1
    return evens
def evaluate_pairs(p1,p2):
    commonality = (len(p1.intersection(p2)))
    return commonality


#End problem 1
print(f"Person 1 selected {evaluate(person1)} evens")
print(f"Person 2 selected {evaluate(person2)} evens")
print(f"Person 3 selected {evaluate(person3)} evens")
print(f"Person 4 selected {evaluate(person4)} evens")
print(f"Person 5 selected {evaluate(person5)} evens")
print(f"Person 6 selected {evaluate(person6)} evens")

print("person 1 and person 2 have" , evaluate_pairs(person1,person2), "views in common")
print("person 1 and person 3 have" , evaluate_pairs(person1,person3), "views in common")
print("person 1 and person 4 have" , evaluate_pairs(person1,person4), "views in common")
print("person 1 and person 5 have" , evaluate_pairs(person1,person5), "views in common")
print("person 1 and person 6 have" , evaluate_pairs(person1,person6), "views in common")
print("person 2 and person 3 have" , evaluate_pairs(person2,person3), "views in common")
print("person 2 and person 4 have" , evaluate_pairs(person2,person4), "views in common")
print("person 2 and person 5 have" , evaluate_pairs(person2,person5), "views in common")
print("person 2 and person 6 have" , evaluate_pairs(person2,person6), "views in common")
print("person 3 and person 4 have" , evaluate_pairs(person3,person4), "views in common")
print("person 3 and person 5 have" , evaluate_pairs(person3,person5), "views in common")
print("person 3 and person 6 have" , evaluate_pairs(person3,person6), "views in common")
print("person 4 and person 5 have" , evaluate_pairs(person4,person5), "views in common")
print("person 4 and person 6 have" , evaluate_pairs(person4,person6), "views in common")
print("person 5 and person 6 have" , evaluate_pairs(person5,person6), "views in common")
