name = "danBrdanendan"

sentence = "My home area is called \"xyz\"" # escape character

print(sentence)

# operations -> functions
print(sentence.upper())
print(sentence)

sentence = sentence.upper()

print(sentence)
print(sentence.capitalize())
print(sentence.title())

print(name.count("dan")) # call a function --using, parameter

print(33, "Tom", "81")

print(len(sentence))

replaced_sentence = sentence.lower().replace("home", "city") # chaining functions

print(replaced_sentence)

k = "123"
# sentence.upper().replace("x", "y").lower().count("s")


print(sentence.isupper()) # boolean True/False
