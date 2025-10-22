class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def grade(self):
        if self.score == 100 and self.score >= 80:
            return f"Name: {self.name}, Grade: A"
        elif self.score <= 79 and self.score >= 70:
            return f"Name: {self.name}, Grade: B"
        elif self.score <= 69 and self.score >= 60:
            return f"Name: {self.name}, Grade: C"
        elif self.score <= 59 and self.score >= 50:
            return f"Name: {self.name}, Grade: D"
        elif self.score < 50:
            return f"Name: {self.name}, Grade: f"
        
stu = student("Ben", 65)
print(stu.grade())