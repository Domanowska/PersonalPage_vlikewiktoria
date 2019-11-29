from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
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

    def test_can_see_artist_links(self):
        # Directly underneath my name they can see an "Artist" button
        # Hovering over the "Artist" button shows a dropdown of different galleries
        self.browser.get('http://localhost:8000')

        artist_dropdown = self.browser.find_element_by_id('artist_drpdn')
        self.assertIn('Artist', artist_dropdown.text)

        ActionChains(self.browser).move_to_element(artist_dropdown).perform()
        gallery_link = self.browser.find_element_by_xpath('//html/body/div[1]/div[1]/a[1]').text
        self.assertIn('Portfolio', gallery_link)

    def test_can_see_engineer_links(self):
        # Directly underneath my name they can see an "Software Engineer" button
        # The "Software Engineer" button has a dropdown that shows a link to my github
        self.browser.get('http://localhost:8000')

        sfteng_dropdown = self.browser.find_element_by_id('sfteng_drpdn')
        self.assertIn('Software Engineer', sfteng_dropdown.text)

        ActionChains(self.browser).move_to_element(sfteng_dropdown).perform()
        github_link = self.browser.find_element_by_xpath('//html/body/div[2]/div[1]/a[1]').text
        self.assertIn('GitHub', github_link)

        # Underneath the dropdowns you can see a few links to social media accounts

        # Underneath the social media links you can see "Contact Me: v.like.wiktoria@gmail.com"


if __name__ == '__main__':
    unittest.main(warnings='ignore')