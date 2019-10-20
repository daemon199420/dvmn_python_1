import os
import smtplib
text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
text = text.replace('%website%', 'dvmn.org')
text = text.replace('%friend_name%', 'Вася')
text = text.replace('%my_name%', 'Саша')
mail = "From: {}\nTo: {}\nSubject: Invite\nContent-Type: text/plain; charset=\"UTF-8\";\n{}"
mail = mail.format('DevmanTest@yandex.ru', 'test@yandex.ru', text).encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
server.login(login, password)
server.sendmail('DevmanTest@yandex.ru', 'test@yandex.ru', mail)
server.quit()

