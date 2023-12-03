#oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''
import random
class student:
    def __init__(self, name, year, student_id, major, gpa ):
        self.name = name
        self.year = year
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
    
p1= student("john","freshman",313,"CS",4.0)
p2 = student("lily","senior",102,"Math",3.5)
p3 = student("Rob","Sophmore",122,"History",2.9)

random_id = random.randint(101, 314)


def check_Honors(student):
    if student.gpa > 3.5:
        print("Congratulations", student.name, "! you are eligible for the honors program.")

    else:
        print("sorry",student.name,"you don't fit the requirements")

def check_lunch(student):
    if student.student_id == random_id:
        print("congrats",student.name,"you have free lunch")

    else:
        print("sorry no free lunch" ,student.name)
    
    
    
def main():

    #create three students and check if they get free lunch and if they qualify for honors
    check_Honors(p1)
    check_lunch(p1)

    check_Honors(p2)
    check_lunch(p2)

    check_Honors(p3)
    check_lunch(p3)

    print("the random id is :",random_id)






main()
