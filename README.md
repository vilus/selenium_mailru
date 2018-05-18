> Авто-тест отправки письма через mail.ru
#
Используемые инструменты:
```bash
selenium
pytest
pytest-selenium
PyPOM
```
#
Установка:
```bash
git clone https://github.com/vilus/selenium_mailru.git
cd selenium_mailru
# virtualenv
pip install -r requirements.txt
```
Настройка браузера: http://pytest-selenium.readthedocs.io/en/latest/user_guide.html#specifying-a-browser
#
Запуск:
```bash
py.test --mail-username "<name@domain>" --mail-password "<password>" --mail-to "<name_to@domain>" --driver="<Browser>" --driver-path "<path/to/driver>"
```
#
Заметки:
```bash
- проверено на win10 + Chrome
```