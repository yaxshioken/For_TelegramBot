# translations.py
translations = {
    'uz': {
        'compony_about_text': '🏢 Kompaniya haqida',
        'menu_text': 'Menyu',
        'savat_text': '🛒 Savat',
        'contact_text': '📞 Kontaktlar/Manzil',
        'lang_text': '🇺🇿/🇷🇺/🇬🇧 Til',
        'ignore_text': '❌ Bekor qilish ❌',
        'back_text': '🔙 ortga',
    },
    'ru': {
        'compony_about_text': '🏢 О компании',
        'menu_text': 'Меню',
        'savat_text': '🛒 Корзина',
        'contact_text': '📞 Контакты/Адрес',
        'lang_text': '🇺🇿/🇷🇺/🇬🇧 Язык',
        'ignore_text': '❌ Отмена ❌',
        'back_text': '🔙 Назад',
    },
    'en': {
        'compony_about_text': '🏢 About Company',
        'menu_text': 'Menu',
        'savat_text': '🛒 Cart',
        'contact_text': '📞 Contacts/Address',
        'lang_text': '🇺🇿/🇷🇺/🇬🇧 Language',
        'ignore_text': '❌ Cancel ❌',
        'back_text': '🔙 Back',
    }
}

def get_translation(lang_code, key):
    return translations.get(lang_code, translations['en']).get(key, key)
