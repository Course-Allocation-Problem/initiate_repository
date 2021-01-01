from course_information import Course_info


class Courses:

    def __init__(self, course_list):
        for i in course_list:
            self.course_list[i] = Course_info(course_list[i])

    def get_course_list(self):
        return self.course_list

    def set_course_list(self, course_list):
        for i in course_list:
            self.course_list[i] = Course_info(course_list[i])

    def over_lap(self):
        for i in self.course_list:
            course_check = self.course_list[i]
            for j in self.course_list:
                if i != j:
                    course_test = self.course_list[j]

                    if course_test.get_time_start() <= course_check.get_time_start() <= course_test.get_time_end():
                        return True

                    elif course_test.get_time_start() <= course_check.get_time_end() <= course_test.get_time_end():
                        return True

        return False
