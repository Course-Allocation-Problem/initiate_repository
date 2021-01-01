from course_information import Course_info


class Course_group:

    def __init__(self, name, url_syllabus, course_list):
        self.name = str(name)
        self.url_syllabus = str(url_syllabus)
        for i in course_list:
            self.course_list[i] = Course_info(course_list[i])

    def get_name(self):
        return self.name

    def get_url_syllabus(self):
        return self.url_syllabus

    def get_course_list(self):
        return self.course_list

    def set_name(self, name):
        self.name = str(name)

    def set_url_syllabus(self, url_syllabus):
        self.url_syllabus = str(url_syllabus)

    def set_course_list(self, course_list):
        for i in course_list:
            self.course_list[i] = Course_info(course_list[i])
