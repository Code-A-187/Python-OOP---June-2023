from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.student1 = StudentReportCard("Test", 4)

    def test_initialisation(self):
        self.assertEqual("Test", self.student1.student_name)
        self.assertEqual(4, self.student1.school_year)
        self.student1.add_grade("Python", 5.00)
        self.assertEqual({'Python': [5.0]}, self.student1.grades_by_subject)

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student1.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_under_1_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student1.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_correct_school_year_1(self):
        self.student1.school_year = 1
        self.assertEqual(1, self.student1.school_year)

    def test_correct_school_year_12(self):
        self.student1.school_year = 12
        self.assertEqual(12,self.student1.school_year)

    def test_wrong_school_years_over_12(self):
        with self.assertRaises(ValueError) as error:
            self.student1.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_add_grade_dict_proper(self):
        self.assertEqual({}, self.student1.grades_by_subject)
        self.student1.add_grade("Python", 5.00)
        self.assertEqual({'Python': [5.0]}, self.student1.grades_by_subject)
        self.student1.add_grade("Python", 6.00)
        self.assertEqual({'Python': [5.0, 6.0]}, self.student1.grades_by_subject)

    def test_average_grade_method_for_subject_on_empty_dict(self):
        result = self.student1.average_grade_by_subject()
        self.assertEqual('', result)

    def test_average_grade_method_for_subject(self):
        self.student1.add_grade("Python", 2)
        self.student1.add_grade("Python", 6.00)
        self.student1.add_grade("Mython", 4.00)
        self.student1.add_grade("Mython", 3.00)
        result = self.student1.average_grade_by_subject()
        self.assertEqual('Python: 4.00\nMython: 3.50', result)

    def test_average_grade_method_for_all(self):
        self.student1.add_grade("Python", 4.00)
        self.student1.add_grade("Python", 6.00)
        self.student1.add_grade("Mython", 5)
        self.student1.add_grade("Mython", 5)
        result = self.student1.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 5.00', result)

    def test_average_grade_method_for_all_with_no_data(self):
        with self.assertRaises(ZeroDivisionError) as error:
            self.student1.average_grade_for_all_subjects()
        self.assertEqual('division by zero', str(error.exception))

    def test_repr(self):
        self.student1.add_grade("Python", 5.99)
        self.student1.add_grade("Python", 6.00)
        self.student1.add_grade("Mython", 4.00)
        self.student1.add_grade("Mython", 3.00)
        result = str(self.student1)
        self.assertEqual('Name: Test\nYear: 4\n----------\nPython: 6.00\nMython: 3.50\n----------\nAverage Grade: 4.75',
                         result)


if __name__ == "__main__":
    main()