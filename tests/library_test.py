from For_MOS.pages.library_page import LibraryPage
import allure


@allure.epic('Негативные проверки входа')
class TestLibrary():
    @allure.story('Проверка страницы авторизации с некорректным логином и паролем')
    def test_incorrectUserNameAndPassword(self, browser):
        library_page = LibraryPage(browser)
        library_page \
            .enterbutton_isExist()\
            .submit_button() \
            .logo_mash_isExist() \
            .logo_catalog_isExist()\
            .logo_materials_isExist() \
            .click_materials() \
            .my_basket_isExist() \
            .lesson_scenarios_isExist() \
            .click_FTTest() \
            .button_edit_FTTS_isExist() \
            .click_edit_FTTest() \
            .button_add_fragment_isExist() \
            .add_video() \
            .delete_lesson() \








