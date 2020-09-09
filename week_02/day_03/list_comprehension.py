# numbers = range(1, 11)
# even_squared = [number * number for number in range(1, 11) if number % 2 == 0]

# for number in numbers:
#     if number % 2 == 0:
#         even_squared.append(number * number)

# print(even_squared)

ages = [5, 15, 64, 27, 84, 26]
odd_ages =[age for age in ages if age % 2 != 0]
print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
more_than_ten =[name for name in chicken_names if len(name) > 10]
print(more_than_ten)
starts_with_h = [name for name in chicken_names if name[0] == ("H" or "h")]
print(starts_with_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
letters = [word[0].lower() for word in words]
print(letters)

