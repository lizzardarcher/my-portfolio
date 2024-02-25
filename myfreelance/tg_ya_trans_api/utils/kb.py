from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_markup(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔶 Админ Панель 🔶", callback_data=f"start:admin"))
    return markup


def del_msg(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    if args == int():
        markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data=f'back:{args[0]}'))
    else:
        markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data=f'back'))
    return markup


def admin_menu_markup(spam, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('❌ Остановить спам', callback_data='menu:mailing:stop')
    btn2 = InlineKeyboardButton('🔥 Подготовить спам', callback_data='menu:mailing:starting:accounts')
    btn3 = InlineKeyboardButton('➕ Добавить чаты списком', callback_data='menu:mailing:starting:add_chats')
    btn4 = InlineKeyboardButton('🗣 Спам по ЛС', callback_data='menu:mailing:starting:lk')
    btn5 = InlineKeyboardButton('👤 Аккаунты', callback_data='menu:account:account_panel')
    btn6 = InlineKeyboardButton('💬 Чаты', callback_data='menu:chat:chat_panel')
    btn7 = InlineKeyboardButton('⚙️ Настройки', callback_data='menu:settings:info')
    btn8 = InlineKeyboardButton('🆘️ Помощь', callback_data='help')
    if spam:
        markup.row(btn1), markup.row(btn3)
    else:
        markup.row(btn2), markup.row(btn3)
    markup.row(btn4)
    markup.row(btn5, btn6)
    markup.row(btn7)
    markup.row(btn8)
    return markup


def get_accounts_markup(accounts, selected_accounts, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('🔥 Запустить спам', callback_data='menu:mailing:start'))

    for account_id, account_name in accounts:
        print(account_id, account_name)
        account_button = InlineKeyboardButton(
            f"{'✅' if str(account_id) in selected_accounts else ''} {account_id} {account_name}",
            callback_data=f"menu:mailing:select_account:{account_id}")
        markup.add(account_button)
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def get_accounts_for_lk_markup(accounts, selected_accounts_for_lk, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('🔥 Запустить спам по ЛС', callback_data='menu:mailing:start_lk'))
    for account_id, account_name in accounts:
        print(account_id, account_name)
        account_button = InlineKeyboardButton(
            f"{'✅' if str(account_id) in selected_accounts_for_lk else ''} {account_id} {account_name}",
            callback_data=f"menu:mailing:select_account_for_lk:{account_id}")
        markup.add(account_button)
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def accounts_panel(*args, **kwargs):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('➕ Добавить аккаунт', callback_data='menu:account:add'))
    # markup.add(InlineKeyboardButton('📑 Скопировать настройки в другой аккаунт', callback_data=f'menu:account:copy_from_settings'))
    markup.add(InlineKeyboardButton('⚙️ Редактировать аккаунты', callback_data='menu:account:search'))
    markup.add(InlineKeyboardButton('🔧 Проверить работоспособность аккаунтов', callback_data='menu:account:check_all'))
    markup.add(InlineKeyboardButton('🔙 Назад', callback_data='back'))
    return markup


def get_all_accounts_markup(accounts, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    print(accounts)
    for account_id, account_name in accounts:
        account_button = InlineKeyboardButton(f"{account_id} @{account_name.split('/')[-1]}",
                                              callback_data=f'menu:account:edit:{account_id}')
        del_button = InlineKeyboardButton(f"❌ Удалить", callback_data=f'menu:account:del_acc:{account_id}')
        markup.row(account_button, del_button)
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def get_account_details(acc_id, is_auto_answering, *args, **kwargs):
    acc_id = str(acc_id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('📝 Изменить спам текст', callback_data=f'menu:account:set_common_text:{acc_id}'))
    markup.add(
        InlineKeyboardButton('📝 Изменить текст автоответчика', callback_data=f'menu:account:set_auto_text:{acc_id}'))
    markup.add(InlineKeyboardButton(f'{"✅" if is_auto_answering else "❌"} Вкл/выкл автоответчик',
                                    callback_data=f'menu:account:set_auto_answer:{acc_id}'))
    markup.add(InlineKeyboardButton('🕔 Изменить таймаут', callback_data=f'menu:account:set_timeout:{acc_id}'))
    markup.add(InlineKeyboardButton('🚫 Сбросить все значения', callback_data=f'menu:account:set_default:{acc_id}'))
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def get_chats_markup(chats, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    for username, chat_id in chats:
        chat_button = InlineKeyboardButton(
            f"@{username.split('/')[-1]} ",
            callback_data=f"menu:chat:chat_details:{chat_id}")
        del_button = InlineKeyboardButton(f"❌ Удалить", callback_data=f'menu:chat:del_chat:{chat_id}')
        markup.add(chat_button, del_button)
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def get_chat_details_markup(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('📝 Изменить текст для чата', callback_data=f'menu:chat:change_chat_text:{chat_id}'))
    markup.add(
        InlineKeyboardButton('🕔 Установить таймаут для чата', callback_data=f'menu:chat:set_chat_timeout:{chat_id}'))
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def get_admins_markup(admins, *args, **kwargs):
    markup = InlineKeyboardMarkup()
    for username, user_id in admins:
        chat_button = InlineKeyboardButton(
            f"{username} ",
            callback_data=f"do_nothing")
        del_button = InlineKeyboardButton(f"❌ Удалить", callback_data=f'menu:settings:delete_admin:{user_id}')
        markup.add(chat_button, del_button)
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup


def settings_panel():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('➕ Добавить Админа', callback_data='menu:settings:add_admin'),
               InlineKeyboardButton('❌ Удалить Админа', callback_data='menu:settings:del_admin'))
    markup.add(InlineKeyboardButton('📞 Изменить текст автоответчика', callback_data='menu:settings:set_auto_answering'))
    markup.add(InlineKeyboardButton('📝 Изменить общий текст', callback_data='menu:settings:set_general_text'))
    markup.add(InlineKeyboardButton('🕔 Изменить таймаут', callback_data='menu:settings:set_timeout'))
    markup.add(InlineKeyboardButton(f'🔙 Назад', callback_data='back'))
    return markup
