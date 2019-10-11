from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_picture_and_name(self):
        # I've told someone about my personal web page I built myself
        # so they decide to check it out and visit my homepage
        self.browser.get('http://localhost:8000')

        # They notice that my page title and header features my handle: v.like.wiktoria
        self.assertIn('v.like.wiktoria', self.browser.title)

        # They see an image showcasing my artwork

        # Directly underneath the image they can see my name

        # Directly underneath my name they can see two dropdowns: "Artist" and "Software Engineer"

        # The "Artist" dropdown shows a link to my gallery

        # The "Software Engineer" dropdown shows a link to my github

        # Underneath the dropdowns you can see a few links to social media accounts

        # Underneath the social media links you can see "Contact Me: v.like.wiktoria@gmail.com"


if __name__ == '__main__':
    unittest.main(warnings='ignore')