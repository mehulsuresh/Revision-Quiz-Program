import random

# Open and read file
data_file = open("questions.txt","r")
data_raw = data_file.read()
data = data_raw.replace("\n", "").split('.')
questions = []
for line in data:
	questions.append(line.split('?'))


#Welcome Message
print("============")
#using ANSI escape sequences for color
print('\033[95m'+"Revison Quiz"+'\033[0m')
print("============")
game_over = False


while game_over != True:
	score = 0
	num_questions = int(input("\nHow many questions would you like? \n:/>"))
	if num_questions > len(questions)-1:
		print ("You dont have that many questions!")
		pass
	else:
		#select x random unique questions
		selected_questions=random.sample(range(0,len(questions)-1), num_questions)
		for x in selected_questions:
			print();
			print("Question ",selected_questions.index(x)+1,":")
			print(questions[x][0],"?", end="")
			answers = questions[x][1].lower().split(", ")
			if len(answers)>1:#If answers are multiple choice
				print("")
				for a in answers: print(a.replace("/",""), end="  ")
				pass
			given_answer = input("\n>")
			if len(answers)>1:
				if '/'+given_answer.lower() in answers:
					print('\033[92m'+"Correct!"+'\033[0m')
					score+=1;
					pass
				else:
					print('\033[91m'+"Incorrect!"+'\033[0m')
					pass


				pass
			else :
				if given_answer.lower() == answers[0].lower():
					print('\033[92m'+"Correct!"+'\033[0m')
					score+=1;
					pass
				else:
					print('\033[91m'+"Incorrect!"+'\033[0m')
					pass
			pass

	print('\033[94m'+"\nYour final score was " + str(score)+"/"+str(num_questions)+'\033[0m')

	#store the user's input...
	again = input('\033[1m'+"Enter any key to play again, or 'q' to quit."+'\033[0m')

    #... and quit if they types 'q'
	if again.lower() == 'q':
		game_over = True
	pass
	