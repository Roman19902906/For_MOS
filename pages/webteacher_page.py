from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from For_MOS.tools.Json.ConfigTools import ConfigTools


class WebPage(BasePage):
    def __init__(self, browser1):
        super().__init__(browser1)

        # Кнопка войти через mos.ru"
        self.enter_mos_ru = lambda: self.browser.find_element_by_xpath(
            "/html/body/div/div[1]/div[1]/main/section/div/div[1]/div[3]/div/div[1]/div[2]/div")
        # Поле логина"
        self.field_login = lambda: self.browser.find_element_by_id("login")
        # Поле пароля"
        self.field_password = lambda: self.browser.find_element_by_id("password")
        # Кнопка Войти"
        self.enter_button = lambda: self.browser.find_element_by_id("bind")
        # Блок организация обучения
        self.study = lambda: self.browser.find_element_by_xpath("//*[.='Организация обучения']")
        # Блок кабинет учителя
        self.room = lambda: self.browser.find_element_by_xpath("//*[.='Кабинет учителя']")
        # Блок библиотека
        self.library = lambda: self.browser.find_element_by_xpath("//*[.='Библиотека']")
        # Кнопка кабинет учителя
        self.button_room = lambda: self.browser.find_element_by_class_name("style_service-teacher-office__nGDRv")
        # Рабочий стол
        self.desk = lambda: self.browser.find_element_by_xpath("//*[.='Рабочий стол']")
        # Кнопка поурочное планирование
        self.plan_lessons = lambda: self.browser.find_element_by_xpath("//*[.='Поурочное планирование']")
        # Кнопка поурочное планирование
        self.plans_lessons = lambda: self.browser.find_element_by_xpath("//*[.='Поурочные планы']")
        # Кнопка поурочное планирование
        self.plan_lessons_and_groups = lambda: self.browser.find_element_by_xpath(
            "//*[.='Связь поурочных планов с группами']")
        # Кнопка поурочное планирование
        self.calendar_plan_lessons = lambda: self.browser.find_element_by_xpath(
            "//*[.='Календарно-тематическое планирование']")
        # Отображение поурочных планов
        self.list_plans = lambda: self.browser.find_element_by_class_name("_22odLFfYvI4xrLi5TIHgjL")
        # Кнопка разработать поурочный план
        self.create_plans = lambda: self.browser.find_element_by_class_name("_3kFIpMZkKbAavsB5_FTrpS")
        # Кнопка создать с нуля
        self.create_new = lambda: self.browser.find_element_by_class_name("dVxICusPGYBj9S5FKz_Js")
        # Выбор поля системный
        self.field_system = lambda: self.browser.find_element_by_xpath("//*[.='Системный']")
        # Выбор поля параллель
        self.field_parallel = lambda: self.browser.find_element_by_class_name("_1RHHA8JbmcDr58ojcwHP49")
        # Выбор параллель
        self.parallel_8 = lambda: self.browser.find_element_by_xpath("//*[.='8']")
        # Выбор поля предмет
        self.field_subject = lambda: self.browser.find_element_by_xpath("//*[.='Выберите предмет...']")
        # Выбор предмета Биология
        self.subject_biology = lambda: self.browser.find_element_by_xpath("/html/body/div[3]/div/div[4]/ul/li[10]")
        # Наименование поурочного плана
        self.plan_subject = lambda: self.browser.find_element_by_class_name("_2iim-RQx66RqKYb9ZyPlH9")
        # Кнопка следующий шаг
        self.next_step = lambda: self.browser.find_element_by_xpath("//*[.='Следующий шаг']")
        # Наведение на кнопку добавить
        self.button_add_vision = lambda: ActionChains(browser1).move_to_element(browser1.find_element_by_class_name("_2SQKB6N9YFCQg-XsbB-1Nk")).perform()
        # Кнопка добавить
        self.button_add = lambda: self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div/div/div/div[1]/button")
        # Выбор темы
        self.select_theme = lambda: self.browser.find_element_by_class_name("_32IZLY1yrAthW4zgb7mGlH")
        # Тема
        self.theme = lambda: self.browser.find_element_by_xpath("/html/body/div[7]/div/div/ul/li[1]")
        # Кнопка сохранить тему
        self.save_theme = lambda: self.browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/main/div/div/div/div/div/div[2]/section/div[2]/div[2]/button[2]")
        # Кнопка структура
        self.button_structure = lambda: self.browser.find_element_by_xpath(
            "/ html / body / div[1] / div[2] / div[2] / main / div / div / aside / header / button")
        # Поле добавить урок
        self.button_add_lesson = lambda: self.browser.find_element_by_xpath("//*[.='Добавить урок']")
        # Поле добавления урока
        self.field_add_subject = lambda: self.browser.find_element_by_xpath(
            "/ html / body / div[1] / div[2] / div[2] / main / div / div / div / div / div / div[2] / section / div / section / div[1] / div[1] / label / div / textarea")
        # Кнопка сохранить урок
        self.save_lesson = lambda: self.browser.find_element_by_xpath("//*[.='Сохранить урок']")

    def enterbutton_isExist(self):
        self.is_element_present(self.enter_mos_ru())
        return self

    def organization_study_isExist(self):
        self.is_element_present(self.study())
        return self

    def room_teacher_isExist(self):
        self.is_element_present(self.room())
        return self

    def library_room_isExist(self):
        self.is_element_present(self.library())
        return self

    def desktop_isExist(self):
        self.is_element_present(self.desk())
        return self

    def plans_lessons_isExist(self):
        self.is_element_present(self.plans_lessons())
        return self

    def plan_lessons_and_groups_isExist(self):
        self.is_element_present(self.plan_lessons_and_groups())
        return self

    def calendar_plan_lessons_isExist(self):
        self.is_element_present(self.calendar_plan_lessons())
        return self

    def list_plan_lessons_isExist(self):
        self.is_element_present(self.list_plans())
        return self

    @allure.step('Кликаем кнопку выбора месяца')
    def click_enter_mos_ru(self):
        self.enter_mos_ru().click()
        return self

    def enter_login_password(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.ID, ("login")))))
        self.field_login().send_keys(ConfigTools.login1())
        self.field_password().send_keys(ConfigTools.password1())
        self.enter_button().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("//*[.='Организация обучения']")))))
        return self

    def enter_room_teacher(self):
        self.button_room().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("//*[.='Рабочий стол']")))))
        return self

    def enter_plan_lessons(self):
        self.plan_lessons().click()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("//*[.='Поурочные планы']")))))
        return self

    def enter_plans_lessons(self):
        self.plans_lessons().click()
        return self

    def create_plans_lessons(self):
        self.create_plans().click()
        return self

    def click_create_plans_new(self):
        self.wait_short.until((EC.element_to_be_clickable(
            (By.CLASS_NAME, ("dVxICusPGYBj9S5FKz_Js")))))
        self.create_new().click()
        return self

    def create_plans_new(self):
        self.field_system().click()
        self.field_parallel().click()
        self.parallel_8().click()
        self.field_subject().click()
        self.subject_biology().click()
        self.plan_subject().send_keys("Биология 8 класс")
        self.next_step().click()
        time.sleep(2)
        self.button_add_vision()
        self.wait_short.until((EC.element_to_be_clickable(
            (By.XPATH, ("/html/body/div[1]/div[2]/div[2]/main/div/div/div/div/div/div[1]/button")))))
        self.button_add().click()
        self.select_theme().click()
        self.theme().click()
        self.save_theme().click()
        return self

    def button_srtructure_new(self):
        self.button_structure().click()
        self.button_add_lesson().click()
        self.field_add_subject().send_keys('Программист "Сервис Монитор"')
        self.save_lesson().click()
        return self
