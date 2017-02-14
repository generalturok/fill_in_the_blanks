'''A Quiz on How Well You know Australian Culture'''


quiz_string1 = '''Australia is was founded in __1__ by Captain James Cook.
The national emblem of Australia shows 2 animals they are: __2__ and __3__.
These animals were chosen because they can not move __4__.'''

quiz_string2 = '''Australia still remains a country in the __5__ of the United Kingdom.
Australia has __6__ States and Territories.'''

parts_of_quiz1 = ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__"]


def word_in_pos(word, parts_of_quiz): #Place the words in the correct order in the strings
    for pos in parts_of_quiz:
        if pos in word:
            return pos
    return None

def play_quiz(ml_string, parts_of_quiz): #Tells user to input words/numbers according to the label (__1__)etc
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_quiz)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_quiz(quiz_string1, parts_of_quiz1)

print play_quiz(quiz_string2, parts_of_quiz1) #The second string and a continuation of the first

