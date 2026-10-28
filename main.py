from API import get_amount
print("what a little we are working.....")

name =  input("please enter your sweet name: ")
quiz = get_amount(5)
score = 1
correct_options = ["a","b","c","d","skip"]

for q in quiz:
	while True:
		print(q["question"])
		for option in q["options"]:
			print(option)
		answer=input("what is your answer 'skip'to skip which takes -2: ").lower()
		if answer == "skip":
			if score <= 1 :
				print("score too low cant let this happen ")
			else:
				print("okay")
				score -=2
				break
		if answer not in correct_options:
			print("enter a valid option you dumbo!!")
		if answer == q["answer"]:
			print("correct answer")
			score += 4
			break
		elif answer =="skip":
			print("")
		elif answer != q["answer"]:
			print(f"wrong asnwr the correct answer is '{q["answer"]}' ")
			score -=1
			break
print(f"HI {name} \n your total is {score}")