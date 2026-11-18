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

r1 = Result()

print("Two Subjects:")
r1.calculate(80, 90)

print("\nThree Subjects:")
r1.calculate(80, 90, 85)
