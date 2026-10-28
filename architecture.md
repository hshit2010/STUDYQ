```mermaid
    flowchart TD
	USER --> UI("enters all info ")
	UI -->test{"test start or not"}
	test --yes--->start("test starts")
	start --> code("runs and loads format and calls API")
	code -->api("gathers sources given by user and makes a test")
	Ui --> user
	user --> correct{"if question correct"}
	correct --yes-->4("+4")
	correct --no -->1("-1")
	correct --skip--> 2("-2")
	4-->total("total points")
	1-->total("total points")
	2-->total("total points")
	test--no -->no("test doesnt start")
	api -->questions{"has the number of questions given by user ended"}
	questions --no -->Ui
	total --> question
	question -->questions
	questions--yes--> end("the end of the test with score")
	end --> USER
```