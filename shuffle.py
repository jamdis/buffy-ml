import random
file = open("buffy-summaries.txt")
text = file.read()
file.close()

list = text.split("|")

print(len(list))
print (list[0])
random.shuffle(list)
print(list[0])

new_text = "|".join(list)

print(new_text)

file = open("buffy-summaries-shuffled.txt", "w+")

file.write(new_text)
file.close()