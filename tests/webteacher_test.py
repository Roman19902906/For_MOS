from For_MOS.pages.webteacher_page import WebPage


class TestWebTeacher():
    def test_date(self, browser1):
        webteacher_page = WebPage(browser1)
        webteacher_page \
            .enterbutton_isExist()\
            .click_enter_mos_ru() \
            .enter_login_password() \
            .organization_study_isExist() \
            .room_teacher_isExist() \
            .library_room_isExist() \
            .enter_room_teacher() \
            .desktop_isExist() \
            .enter_plan_lessons() \
            .plans_lessons_isExist() \
            .plan_lessons_and_groups_isExist() \
            .calendar_plan_lessons_isExist() \
            .enter_plans_lessons() \
            .create_plans_lessons() \
            .click_create_plans_new() \
            .create_plans_new() \
            .button_srtructure_new()\


