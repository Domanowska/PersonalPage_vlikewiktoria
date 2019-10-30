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

        # They notice that my page title features my handle: v.like.wiktoria
        self.assertIn('v.like.wiktoria', self.browser.title)

        # They see an image showcasing my artwork
        showcase_image = self.browser.find_element_by_tag_name('img')
        self.assertNotEqual(showcase_image.get_attribute("naturalWidth"), '0')

        # Directly underneath the image they can see my name
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Wiktoria Domanowska', header_text)

        # Directly underneath my name they can see two buttons: "Artist" and "Software Engineer"
        artist_dropdown = self.browser.find_element_by_class_name('dropdown').text
        self.assertIn('Artist', artist_dropdown)

        # The "Artist" button has a dropdown that shows a link to my gallery

        # The "Software Engineer" button has a dropdown that shows a link to my github

        # Underneath the dropdowns you can see a few links to social media accounts

        # Underneath the social media links you can see "Contact Me: v.like.wiktoria@gmail.com"


if __name__ == '__main__':
    unittest.main(warnings='ignore')