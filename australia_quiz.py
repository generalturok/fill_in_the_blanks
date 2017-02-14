'''A Quiz on How Well You know Australian Culture'''
#opening sentence to explain what the program is and what it is about
print "Play my Australia, fill in the blanks game!"'\n'
#Including 3 levels: easy/medium/hard
easy_question = '''Australia was founded in __1__ by Captain James Cook.
The national emblem of Australia shows 2 animals they are: __2__ and __3__.
These animals were chosen because they can not move __4__.\n'''
easy_answers = ['1777','kangaroo','emu','back']
medium_question = '''Australia still remains a country in the __1__ of the United Kingdom.
Australia has __2__ States and Territories. They are NSW,VIC,SA,WA,NT,ACT,__3__,__4__.\n'''
medium_answers = ['commonwealth','8','TAS','QLD']
hard_question = '''Famous Australian athletes and sportspersons include: Cathy __1__, __2__ Ablett, Donald __3__,
__4__ Bogut.\n'''
hard_answers = ['Freeman','Gary','Bradman','Andrew']
#Using blanks __1__-__4__ is easier to sort then going all the way up to 20.
#This was made possible by placing the questions and answers for easy-hard in seperate classes/strings.
blanks = ["__1__","__2__","__3__","__4__"]

user_input = raw_input("Select a difficulty: easy, medium, hard \n")
user_input=user_input.lower()

#Sets up the difficulty setting for the user. If the word is not either easy,medium or hard.
#The user is forced to re-enter their input.
def difficulty(user_input):
    level_list=["easy","medium","hard"]
    while user_input not in level_list:
        user_input = raw_input("Please select one of the 3 options: easy, medium or hard \n")
        user_input=user_input.lower()
    if user_input in level_list:
        user_chances=raw_input("How many 'CHANCES' will you need? \n ")
        user_chances=int(user_chances)
        return user_input,user_chances

#This function correalates both the answers and the question to the appropriate blanks.
#ie: easy questiion to easy answer
def question_answer(levelinput):
    if levelinput == "easy":
        return easy_answers, easy_question
    elif levelinput == "medium":
        return medium_answers,medium_question
    elif  levelinput == "hard":
        return hard_answers,hard_question


level,user_chances = difficulty(user_input)
answerlist,question=question_answer(level)


#function informs the user if their guesss is true or false and how many chances they have.
#There is a else statement which explains when they are wrong and when it is game over
def fill_in_the_blank(question, answerlist, blank):
    print "\nFill in the Blank:   "+ question
    i,guess = 0,0
    while (i < len(answerlist)) and (guess < user_chances) :
         answer = raw_input("What is the missing word/number" + blank[i]+ "? \n")
         if answer == answerlist[i]:
             print "Correct! \n"
             question = question.replace("_"+blank[i]+"_",answerlist[i])
             print question
             i =i + 1
             if i == len(answerlist):
                print "Congratulations! You are a true Australian!! Try at a different level next time ;)"
         else:
              print "Try Again \n"
              guess=guess + 1
              if guess == user_chances:
                print "Too bad , your  " + str(user_chances) + " chances are over and unfortunately game is over."

fill_in_the_blank(question,answerlist,blanks)