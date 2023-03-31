import unittest
import HtmlTestRunner

from Class_Check_Element import Check_text_element
from Class_Check_Page import Check_page
from Class_Login import Login


class TestSuite(unittest.TestCase):
    tests_to_run = unittest.TestSuite()
    tests_to_run.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Check_page),
                           unittest.defaultTestLoader.loadTestsFromTestCase(Check_text_element),
                           unittest.defaultTestLoader.loadTestsFromTestCase(Login)])

    runner = HtmlTestRunner.HTMLTestRunner(
        combine_reports=True,
        report_title="Test Execution Report",
        report_name="Test Results")

    runner.run(tests_to_run)