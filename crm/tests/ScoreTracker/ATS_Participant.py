import time
import unittest
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "Golfer_1"
       pwd = "maverick1a"
       course_name = "Eagle Run"
       hole_score ='1'
       total_score = "18"
       golf_date = '04/30/2020'
       driver = self.driver
       driver.maximize_window()
       driver.get("https://frenemies-scoretracker.herokuapp.com/accounts/login/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://frenemies-scoretracker.herokuapp.com/home/")
       assert "Logged In"
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div[2]/div/div/p[2]/a").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_course_name")
       elem.send_keys(course_name)
       elem = driver.find_element_by_id("id_user")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_hole_one")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_two")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_three")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_four")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_five")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_six")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_seven")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_eight")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_nine")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_ten")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_eleven")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_twelve")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_thirteen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_fourteen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_fifteen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_sixteen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_seventeen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_hole_eighteen")
       elem.send_keys(hole_score)
       elem = driver.find_element_by_id("id_total_score")
       elem.send_keys(total_score)
       elem = driver.find_element_by_id("id_golf_date")
       elem.send_keys(golf_date)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[1]/a").click()
       time.sleep(1)
       # Select Courses
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
       time.sleep(1)
       #Select Score Compare
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[2]/td[4]/a").click()
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()