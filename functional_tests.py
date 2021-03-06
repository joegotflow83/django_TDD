from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing env"""
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)


	def tearDown(self):
		"""Tear down testing env"""
		self.browser.quit()


	def test_can_start_a_list_and_retrieve_it_later(self):
		"""Test a user can open up the web page and access the first page"""
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main()