
with open("story.txt", "r") as f:
    #gives all the text in the file
    story = f.read()

words = set() #using set here instead of a list[] to make the contents unique,i.e without repetition
start_of_word = -1

target_start = "<"
target_end = ">"

#look for all the words in the story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1


answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)