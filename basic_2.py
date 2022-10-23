first_number = 2.0001
second_number = 5
third_number = first_number / second_number
print(third_number)
print(round(third_number))
print(round(third_number,4))

print(round(2.5))
print(round(3.5))

age = 22
weight = 67
isMarried = False
result_Married = age == 21 or isMarried
result = age > 21 and weight == 67
print(not age > 21)
print (not isMarried)
print (result)
print (result_Married)

msg = "Hello world!"
search_word = "Hello"
invers_word = "hello"
result_search = search_word in msg
inv_result_search = invers_word not in msg
print(result_search)
print(inv_result_search)


language_1 = "russian"
language_2 = "english"

if language_1 != language_2:
    print(language_1)
else:
    print(language_2)

language = "french"
if language == "english":
    print("Hello")
elif language == "german":
    print("Hallo")
elif language == "french":
    print("Salut")
else:
    print("Привет")

language = "english"
daytime = "morning"
if language == "english":
    if daytime == "morning":
        print("Good morning")
    else:
        print("Good evening")
else:
    if daytime == "morning":
        print("Доброе утро")
    else:
        print("Добрый вечер")

print("z = ",248007-42315)