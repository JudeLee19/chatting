from functional_tests.base import FunctionalTest
import os


class FileTest(FunctionalTest):

    def test_can_save_file_in_message(self):
        # execute browser
        self.login()

        self.post_issue_channel()
        div = self.browser.find_element_by_class_name('sorted_issue_list')
        issue_channels = div.find_elements_by_tag_name('a')
        issue_1 = issue_channels[0]
        issue_1.click()
        # User can check + Button in message view and if the user click + button, file upload button is showed
        messages_input_container = \
            self.browser.find_element_by_id('messages_input_container')
        plus_btn = messages_input_container.find_element_by_id('btn_plus')
        self.assertEqual(plus_btn.get_attribute("class"), "messages_input_plus")
        plus_btn.click()

        file_upload_btn = self.browser.find_element_by_id('item_upload_file')
        file_upload_btn.click()
        # When file upload button is clicked, the form is showed.
        file_title = self.browser.find_element_by_id('id_title')
        file_title.send_keys('Test_File_Upload')

        file_select_btn = self.browser.find_element_by_id('id_file')
        file_select_btn.send_keys(os.getcwd()+'/test_file')

        # If submit button the file is uploaded into message.
        btn_file_submit = self.browser.find_element_by_id('btn_file_submit')
        btn_file_submit.click()