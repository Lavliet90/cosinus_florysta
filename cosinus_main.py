import json


class Lectures:
    def __init__(self, name, teacher, total_hours, hours_passed, hours_attended, estimates, additional_info):
        self.name = name
        self.teacher = teacher
        self.total_hours = total_hours
        self.hours_passed = hours_passed
        self.hours_attended = hours_attended
        self.estimates = estimates
        self.additional_info = additional_info


class LecturesTracker:
    def __init__(self, courses):
        self.courses = courses

    def count_attended_hours(self):
        attended_hours = 0
        for course in self.courses:
            attended_hours += course.hours_attended
        return attended_hours


    def update_hours_attended(self, course_name, hours_attended):
        for course in self.courses:
            if course.name == course_name:
                course.hours_attended = hours_attended
                with open('lectures_on_floristry.json', 'w') as f:
                    json.dump(data, f, indent=4)
                break

with open('lectures_on_floristry.json', 'r') as f:
    data = json.load(f)

courses = []
for course_name, course_data in data.items():
    course = Lectures(
        course_name, course_data['teacher'], course_data['total hours'],
        course_data['hours have passed'], course_data['how many hours i was'],
        course_data['estimates'], course_data['additional Information'])
    courses.append(course)

tracker = LecturesTracker(courses)
attended_hours = tracker.count_attended_hours()
print(f'Total attended hours: {attended_hours}')

# Update hours attended for a course
tracker.update_hours_attended('Kompozycje florystyczne', 2)


