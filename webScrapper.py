import requests
from bs4 import BeautifulSoup


class WebScrapper:

    def __init__(self):
        self.baseURL = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course'
        self.queryParameters = '&dept=COMM&course=290'
        pass

    def getCourseTable(self):
        page = requests.get(self.baseURL + self.queryParameters)
        soup = BeautifulSoup(page.content, 'html.parser')
        courseTable = soup.findAll(
            'table', class_='table table-striped section-summary')[0].findAll('tr')
        # courseTable = soup.find(
        #     'table', class_='table table-striped section-summary')
        # listOfSections = courseTable.findAll('tr')
        return courseTable[1:]

    # Finds all activities that are either a Lecture or a Web-Oriented Course
    def findLectures(self, courseTable):
        listOfLectures = []
        for activity in courseTable:
            activityType = activity.findAll('td')[2].text
            if activityType == "Lecture" or activityType == "Web-Oriented Course":
                listOfLectures.append(activity)
        return listOfLectures

    def isLectureOpen(self, lecture):
        isOpen = (True if len(lecture.findAll('td')[0].text) == 0 else False)
        return isOpen

    def isLectureRestricted(self, lecture):
        isRestricted = (True if lecture.findAll(
            'td')[0].text == 'Restricted' else False)
        return isRestricted


'''
1. Retrieve the course table given course code and course ID
2. Find all available lectures
3. Filter lectures to find lectures that have open spots available
'''


def main():
    scrapper = WebScrapper()
    courseTable = scrapper.getCourseTable()
    lectures = scrapper.findLectures(courseTable)
    openLectures = []
    restrictedLectures = []
    for l in lectures:
        if scrapper.isLectureOpen(l):
            openLectures.append(l)
        elif scrapper.isLectureRestricted(l):
            restrictedLectures.append(l)
    pass


if __name__ == '__main__':
    main()
