class Student:

    def __init__(self, name, id_student, email, score, amount_elective, rank, result):
        self.name = str(name)
        self.id_student = str(id_student)
        self.email = str(email)
        self.score = int(score)
        self.amount_elective = int(amount_elective)
        self.rank = rank  # Need to add castering to it
        self.result = result  # Need to add castering to it

    def get_name(self):
        return self.name

    def get_id_student(self):
        return self.id_student

    def get_email(self):
        return self.email

    def get_score(self):
        return self.score

    def get_amount_elective(self):
        return self.amount_elective

    def get_rank(self):
        return self.rank

    def get_result(self):
        return self.result

    def set_name(self, name):
        self.name = str(name)

    def set_id_student(self, id_student):
        self.id_student = str(id_student)

    def set_email(self, email):
        self.email = str(email)

    def set_score(self, score):
        self.score = int(score)

    def set_amount_elective(self, amount_elective):
        self.amount_elective = int(amount_elective)

    def set_rank(self, rank):
        self.rank = rank    # Need to add castering to it

    def set_result(self, result):
        self.result = result    # Need to add castering to it
