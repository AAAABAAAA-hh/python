class Doctor(object):
    def __init__(self, name, age,job,gender,sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal
    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False
        else:
            return self.name == other.name and self.job == other.job and self.gender == other.gender and self.sal == other.sal

doc_1 = Doctor("ming",29,"doc","man",10000)
doc_2 = Doctor("ming",29,"doc","man",20000)
doc_3 = Doctor("ming",29,"doc","man",20000)

print("doc_1 == doc_2:",doc_1.__eq__(doc_2))
print("doc_1 == doc_3:",doc_1.__eq__(doc_3))
print("doc_2 == doc_3:",doc_2.__eq__(doc_3))





