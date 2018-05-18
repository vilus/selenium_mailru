# -*- coding: utf-8 -*-
from pages import MailruPage


def test_send_via_mailru(selenium, mail_opts):
    mailru_pg = MailruPage(selenium, mail_opts.url).open()
    mailru_pg.mailbox.login(mail_opts.username, mail_opts.password)

    letter_pg = mailru_pg.mailbox.new_letter()
    letter_pg.fill_fields(mail_opts.to, mail_opts.body)
    letter_pg.send()
