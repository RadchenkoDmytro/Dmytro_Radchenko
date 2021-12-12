import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Chromedriver\\chromedriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        #Авторизація на сайті
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("txtUsername").send_keys("Admin")       
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        #Перехід до робочих змін
        driver.find_element_by_id("menu_admin_viewAdminModule").click()
        driver.find_element_by_id("menu_admin_Job").click()
        driver.find_element_by_id("menu_admin_workShift").click()

        #Створення нового запису
        driver.find_element_by_id("btnAdd").click()
        driver.find_element_by_id("workShift_name").send_keys("Dmytro")
        driver.find_element_by_xpath("//select[@id='workShift_workHours_from']/option[@value='06:00']").click()
        driver.find_element_by_xpath("//select[@id='workShift_workHours_to']/option[@value='18:00']").click()
        driver.find_element_by_id("workShift_availableEmp").send_keys(Keys.CONTROL + 'a')
        driver.find_element_by_id("btnAssignEmployee").click()
        driver.find_element_by_id("btnSave").click()

        #Перевірка наявності новоствореного запису
        available = False
        deleteRow = None
        rows_list = driver.find_element_by_id('resultTable').find_elements_by_tag_name('tr')
        for row in rows_list:
            cols_list = list(row.find_elements_by_tag_name('td'))  
            if len(cols_list)>3 and cols_list[1].text =='Dmytro' and cols_list[2].text =='06:00' and cols_list[3].text =='18:00' and cols_list[4].text == '12.00':
                available = True
                deleteRow = row
                break

        import time
        time.sleep(3)
        #Видалення поля за наявності у таблиці
        if available:
            deleteRow.find_element_by_tag_name('input').click()
            driver.find_element_by_id('btnDelete').click()
            driver.find_element_by_id('dialogDeleteBtn').click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()