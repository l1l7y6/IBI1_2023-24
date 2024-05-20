class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score
    
    def print_student_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio: {self.code_portfolio_score}, "
              f"Group Project: {self.group_project_score}, Exam Score: {self.exam_score}")

# Example usage:
student1=Student("Li Yilan", "BMI", 100, 100, 100)
student1.print_student_details()