# -*- coding: utf-8 -*-
from pypom import Page, Region
from selenium.webdriver.common.by import By


class MailruPage(Page):
    """mail.ru"""

    @property
    def mailbox(self):
        return MailboxRegion(self)


class MailboxRegion(Region):
    """mailbox container in top-left"""

    def login(self, username, password):
        MailboxLoginRegion(self.page).signup(username, password)
        mailbox_pg = MailboxPage(self.driver)
        mailbox_pg.wait_for_page_to_load()
        return self.page.open()

    def new_letter(self):
        MailboxMenuRegion(self.page).click_write_letter()
        return LetterPage(self.driver).wait_for_page_to_load()


class MailboxMenuRegion(Region):
    _write_letter_link = (By.ID, 'mailbox:write_letter')

    def click_write_letter(self):
        self.find_element(*self._write_letter_link).click()


class MailboxLoginRegion(Region):
    _username_field = (By.ID, 'mailbox:login')
    _password_field = (By.ID, 'mailbox:password')
    _signin_label = (By.ID, 'mailbox:submit')

    def type_username(self, username):
        self.find_element(*self._username_field).send_keys(username)

    def type_password(self, password):
        self.find_element(*self._password_field).send_keys(password)

    def click_signin(self):
        self.find_element(*self._signin_label).click()

    def signup(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_signin()


class MailboxPage(Page):
    @property
    def loaded(self):
        # TODO: improve
        return 'messages/inbox' in self.driver.current_url


class LetterPage(Page):
    @property
    def loaded(self):
        # TODO: improve
        return 'compose' in self.driver.current_url

    def send(self):
        LetterToolbarRegion(self).click_send_button()
        self.wait.until(lambda _: 'sendmsgok' in self.driver.current_url)

    def fill_fields(self, to, body):
        letter = LetterComposeRegion(self)
        letter.type_to(to)
        letter.type_body(body)


class LetterToolbarRegion(Region):
    _send_button = (By.XPATH, '//div[@data-name="send"]')

    def click_send_button(self):
        self.find_element(*self._send_button).click()


class LetterComposeRegion(Region):
    _to_field = (By.XPATH, '//textarea[@data-original-name="To"]')
    _body_frame = (By.XPATH, '//iframe[contains(@id, "composeEditor_ifr")]')
    _body_field = (By.ID, 'tinymce')

    def type_to(self, to):
        self.find_element(*self._to_field).send_keys(to)

    def type_body(self, body):
        body_frame = self.find_element(*self._body_frame)
        self.driver.switch_to.frame(body_frame)
        self.find_element(*self._body_field).send_keys(body)
        self.driver.switch_to.default_content()
