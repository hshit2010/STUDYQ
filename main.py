name =  input("please enter your sweet name: ")
quiz = [
	{
		"question":"whats the atomic number of hydrogen'H'",
		"options":["a.2","b.5","c.7","d.1"],
		"answer":"d"
	},
	
	{
	   "question":"capital of INDIA",
	   "options":["a.delhi","b.mumbai","c.chandigarh","d.washington D.C."],
	   "answer":"a" 
	},
	{
		   "question":"the derivative of 2x^2",
		   "options":["a.4x","b.6x","c.4x^2","d.10y"],
		   "answer":"a" 
		},
	{
		   "question":"capital of U.S.A",
		   "options":["a.delhi","b.chichago","c.washington D.C.","d.new york"],
		   "answer":"c" 
		}
]
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