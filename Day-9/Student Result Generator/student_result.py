#Student Result Generator (Method Overloading Concept) 
#A school system calculates student results differently depending on available data. 
#Create a Result class where a method can calculate the result using either two 
#subjects or three subjects.

class Result:
    def calculate(self, mark1, mark2, mark3=None):
        if mark3 is None:
            total = mark1 + mark2
            average = total / 2
        else:
            total = mark1 + mark2 + mark3
            average = total / 3

        print("Total Marks:", total)
        print("Average:", average)


r = Result()

r.calculate(80, 90)
r.calculate(80, 90, 85)
