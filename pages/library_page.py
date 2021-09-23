import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage
from For_MOS.tools.Json.ConfigTools import ConfigTools
from selenium.webdriver.support import expected_conditions as EC


class LibraryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.move_mouse = lambda: ActionChains(browser).move_to_element(browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[4]/div[2]/div")).perform()
        # Отображение кнопки войти
        self.button = lambda: self.browser.find_element_by_class_name("loginButton_z0CRQR")
        # Логотип "Библиотека МЭШ"
        self.logo_mash = lambda: self.browser.find_element_by_id("library-logo-unique-identifier")
        # Логотип "Каталог"
        self.logo_catalog = lambda: self.browser.find_element_by_class_name("link_1rnIi0")
        # Логотип "Матреиалы"
        self.logo_materials = lambda: self.browser.find_element_by_css_selector("button.link_1rnIi0")
        # Папка "Моя корзина"
        self.my_basket = lambda: self.browser.find_element(By.CSS_SELECTOR, "[title='Моя корзина']")
        # Папка "Сценарии уроков"
        self.lesson_scenarios = lambda: self.browser.find_element_by_css_selector("[title='Сценарии уроков']")
        # Кнопка "FTTS"
        self.button_FTTS = lambda: self.browser.find_element_by_xpath("//*[.='FTTest']")
        # Кнопка редактировать в окне "FTTS"
        self.button_correct_FTTS = lambda: self.browser.find_element_by_xpath("//*[.='Редактировать']")

        self.check_box = lambda: self.browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[1]/div[2]/div[3]/div[3]/button")
        # Кнопка войти
        self.button_enter = lambda: self.browser.find_element_by_class_name("loginButtonWrap_939jb3")
        # Кнопка авторизации по логину и паролю
        self.button_enter_login_password = lambda: self.browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[1]/div[2]/div[2]/div/button")
        # Поле логина
        self.field_login = lambda: self.browser.find_element_by_id("login-field")
        # Поле пароля
        self.field_password = lambda: self.browser.find_element_by_id("password-field")
        # Кнопка войти окна ввода логина и пароля
        self.button_submit = lambda: self.browser.find_element_by_class_name("buttonsWrap_gdlF09")
        # Переключение на окно с редактированием
        self.window = lambda: self.browser.switch_to.window(browser.window_handles[1])
        # Checkbautton javascript в окне редактирование "FTTS"
        self.checkbutton = lambda: self.browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[1]/div[2]/div[3]/div[1]/div/div[1]")
        # Кнопка закрыть javascript в окне редактирование "FTTS"
        self.button_close = lambda: self.browser.find_element_by_xpath("./html/body/div[2]/div/div[1]/div[1]")
        # Кнопка добавить фрагмент в окне редактирование "FTTS"
        self.button_add_fragment = lambda: self.browser.find_element_by_xpath("//*[.='Добавить фрагмент']")
        # Кнопка изменить фрагмент в окне редактирование "FTTS"
        self.button_change_fragment = lambda: self.browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[4]/div[2]/div")
        # Кнопка медиа
        self.button_add_media = lambda: self.browser.find_element_by_xpath("//*[.='Медиа']")
        # Кнопка видео
        self.button_add_video = lambda: self.browser.find_element_by_xpath("//*[.='Видео']")
        # Кнопка выбора видео
        self.button_select_video = lambda: self.browser.find_element_by_xpath(
            "./html/body/div[2]/div/div[1]/div/div[5]/div/div[1]/div/ul/li[1]/div[2]/div[1]")
        # Кнопка Добавить в урок
        self.button_add_video_in_lesson = lambda: self.browser.find_element_by_xpath("//*[.='Добавить в урок']")
        # Проверка наличия видео
        self.check_video_in_lesson = lambda: self.browser.find_element_by_id("cktu2l5p1001n3568iaalh7dp")
        # Кнопка сохранить в урок
        self.save_lesson = lambda: self.browser.find_element_by_xpath("//*[.='Сохранить']")
        # Проверка сохранения урока
        self.check_save_lesson = lambda: self.browser.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[4]/div[2]/div/img")
        # Удаление сценария
        self.del_scenarios = lambda: self.browser.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[3]')
        # Поп ап
        self.pop_ap = lambda: self.browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[3]')

    def wait_calendar_button(self):
        self.wait_short.until(lambda browser: not self.pop_ap().is_displayed())
        return self

    def enterbutton_isExist(self):
        self.is_element_present(self.button())
        return self

    def submit_button(self):
        self.button_enter().click()
        self.button_enter_login_password().click()
        self.field_login().send_keys(ConfigTools.login())
        self.field_password().send_keys(ConfigTools.password())
        self.button_submit().click()
        return self

    def click_materials(self):
        self.logo_materials().click()
        return self

    def click_FTTest(self):
        self.is_element_present(
            self.wait_short.until((EC.element_to_be_clickable((By.XPATH, ("//*[.='FTTest']"))))))
        self.button_FTTS().click()
        self.wait_short.until((EC.element_to_be_clickable((By.XPATH, ("//*[.='Редактировать']")))))
        return self

    def click_edit_FTTest(self):
        self.button_correct_FTTS().click()
        self.window()
        self.wait_short.until((EC.element_to_be_clickable((By.XPATH, ("//*[.='Следующий']")))))
        self.checkbutton().click()
        self.button_close().click()
        return self

    def add_video(self):
        self.button_change_fragment().click()
        self.button_add_media().click()
        self.button_add_video().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("./html/body/div[2]/div/div[1]/div/div[5]/div/div[1]/div/ul/li[1]/div[2]/div[1]")))))
        self.button_select_video().click()
        self.button_add_video_in_lesson().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("//*[.='Сохранить']")))))
        self.save_lesson().click()
        return self

    def delete_lesson(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, (
                "/ html / body / div[1] / div[1] / div[2] / div[1] / div / div[1] / div[1] / div / div[2] / div[2] / div[2] / div / div / div / div[2] / div[4] / div[2] / div")))))
        self.move_mouse()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, (
                "/ html / body / div[1] / div[1] / div[2] / div[1] / div / div[1] / div[1] / div / div[2] / div[2] / div[2] / div / div / div / div[2] / div[3]")))))
        self.del_scenarios().click()
        self.save_lesson().click()
        self.save_lesson().get_property('disabled')
        return self

    def logo_mash_isExist(self):
        self.is_element_present(
            self.wait_short.until((EC.element_to_be_clickable((By.ID, "library-logo-unique-identifier")))))
        return self

    def logo_catalog_isExist(self):
        self.is_element_present(self.logo_catalog())
        return self

    def logo_materials_isExist(self):
        self.is_element_present(self.logo_materials())
        return self

    def my_basket_isExist(self):
        self.is_element_present(
            self.wait_short.until((EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Моя корзина']")))))
        return self

    def lesson_scenarios_isExist(self):
        self.is_element_present(self.lesson_scenarios())
        return self

    def button_edit_FTTS_isExist(self):
        self.is_element_present(self.button_correct_FTTS())
        return self

    def button_add_fragment_isExist(self):
        self.is_element_present(self.button_add_fragment())
        return self

    def check_video_in_lesson_isExist(self):
        self.is_element_present(self.check_video_in_lesson())
        return self

    def check_save_lesson_isExist(self):
        self.is_element_present(self.check_save_lesson())
        return self

    def check_add_fragment_isExist(self):
        self.is_element_present(self.button_add_fragment())
        return self
