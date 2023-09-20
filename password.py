import urwid


def has_digit(password):
    if any(i.isdigit() for i in password):
        return True
    return False


def is_very_long(password):
    if len(password) > 12:
        return True
    return False


def has_letters(password):
    if any(i.isalpha() for i in password):
        return True
    return False


def has_upper_letters(password):
    if any(i.isupper() for i in password):
        return True
    return False


def has_lower_letters(password):
    if any(i.islower() for i in password):
        return True
    return False


def has_symbols(password):
    if any(not i.isalpha() and not i.isdigit() for i in password):
        return True
    return False


functional_list = [has_digit, is_very_long, has_letters, has_upper_letters, has_lower_letters, has_symbols]


def on_ask_change(edit, new_edit_text):
    score = 0
    for i in functional_list:
        if i(new_edit_text):
            score += 2
    reply.set_text("Безопасность пароля: %s" % score)


ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()
