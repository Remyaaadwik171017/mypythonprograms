sub1=int(input("Enter your marks for sub1: "))
sub2=int(input("Enter your marks for sub1: "))
sub3=int(input("Enter your marks for sub1: "))
sub4=int(input("Enter your marks for sub1: "))
total_marks=200
got_marks=sub1+sub2+sub3+sub4
per=(got_marks*100)/total_marks
if per>=90:
    print("you got A+ with percentage of",per)
elif 80<=per<=89:
    print("you got:A.with percentage ",per)
elif 70<=per<=79:
    print("you got:B+. with percentage ",per)
elif 60<=per<=69:
    print("you got:B. with percentage ",per)
elif 50<=per<=59:
    print("you got: c+. with percentage ",per)
elif 40<=per<=49:
    print("you got:C. with percentage ",per)
elif 30<=per<=39:
    print("you got:D+.with percentage ",per)
else:
    print("you failed",per)
