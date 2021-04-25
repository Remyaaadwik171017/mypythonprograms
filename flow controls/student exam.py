classheld=int(input("Enter the no of classes you are attended:"))
attendance=int(input("Enter the total no of classes:"))
class1=(classheld*100)/attendance
if class1<75:
    print("you are not allowed to attend the Exam")
else:
    print("You can write the exam")