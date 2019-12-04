from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_can_see_picture_and_name(self):
        # I've told someone about my personal web page I built myself
        # so they decide to check it out and visit my homepage
        # They notice that my page title features my handle: v.like.wiktoria
        self.assertIn('v.like.wiktoria', self.browser.title)

        # They see an image showcasing my artwork
        showcase_image = self.browser.find_element_by_tag_name('img')
        self.assertNotEqual(showcase_image.get_attribute("naturalWidth"), '0')

        # Directly underneath the image they can see my name
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Wiktoria Domanowska', header_text)

    def test_can_visit_artist_links(self):
        # Directly underneath my name they can see an "Artist" button
        # Hovering over the "Artist" button shows a dropdown of different galleries
        artist_dropdown = self.browser.find_element_by_id('artist_drpdn')
        self.assertIn('Artist', artist_dropdown.text)

        ActionChains(self.browser).move_to_element(artist_dropdown).perform()
        gallery_link = self.browser.find_element_by_xpath('//html/body/div[1]/div[1]/a[1]')
        self.assertIn('Portfolio', gallery_link.text)
        link_text = gallery_link.get_attribute("href")
        self.assertEqual('http://localhost:8000/gallery', link_text)

    def test_can_see_engineer_links(self):
        # Directly underneath my name they can see an "Software Engineer" button
        # The "Software Engineer" button has a dropdown that shows a link to my github
        sfteng_dropdown = self.browser.find_element_by_id('sfteng_drpdn')
        self.assertIn('Software Engineer', sfteng_dropdown.text)

        ActionChains(self.browser).move_to_element(sfteng_dropdown).perform()
        github_link = self.browser.find_element_by_xpath('//html/body/div[2]/div[1]/a[1]')
        self.assertIn('Blog', github_link.text)

        # Underneath the dropdowns you can see a few links to social media accounts

        # Underneath the social media links you can see "Contact Me: v.like.wiktoria@gmail.com"


if __name__ == '__main__':
    unittest.main(warnings='ignore')