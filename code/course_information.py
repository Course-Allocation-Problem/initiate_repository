import datetime


class Course_info:

    def __init__(self, course_id, lecturer, capacity, ):
        self.course_id = str(course_id)
        self.lecturer = str(lecturer)
        self.capacity = int(capacity)
        self.time_start = datetime.datetime(18, 00)
        self.time_end = datetime.datetime(18, 00)  # need to change the time

    def set_course_id(self, course_id):
        self.course_id = str(course_id)

    def set_lecturer(self, lecturer):
        self.lecturer = str(lecturer)

    def set_capacity(self, capacity):
        self.capacity = int(capacity)

    def set_time_start(self, time_start):
        self.time_start = datetime(time_start)

    def set_time_end(self, time_end):
        self.time_end = datetime(time_end)

    def get_course_id(self):
        return self.course_id

    def get_lecturer(self):
        return self.lecturer

    def get_capacity(self):
        return self.capacity

    def get_time_start(self):
        return self.time_start

    def get_time_end(self):
        return self.time_end

    def to_string(self):
        return "course id: ", self.course_id, " lecturer name: ", self.lecturer, "\n",\
               "capacity of the class: ", self.capacity, "\n", \
               "the hour that the lesson start: ", self.time_start, "\n", \
               "the hour that the lesson end: ", self.time_end
