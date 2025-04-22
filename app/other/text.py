import re
import logging
from decimal import Decimal, InvalidOperation
from decimal import InvalidOperation
from app.other.classes import GetData
from decimal import Decimal
from aiogram.utils.markdown import text, bold, code


async def set_text():
    r"""
    Формирует текстовое сообщение с котировками валют.
    
    :return: Строка с котировками валют.
    """
    gd = GetData()
    res: dict = await gd()
    logging.info(f"Данные от GetData: {res}")

    # Проверка наличия всех необходимых ключей
    required_keys = ['investing', 'abcex', 'centralb', 'xe_usd',
                     'centralb_eur', 'xe_e_r', 'centralb_cny', 'xe_cny', 'xe_eur']
    if not all(key in res for key in required_keys) or 'price' not in res.get('investing', {}):
        logging.error(f"Недостаточно данных в res: {res}")
        return "Ошибка: неполные данные котировок"

    ch: dict = await price_correction(res)
    if ch is None:
        logging.error(f"price_correction вернул None для данных: {res}")
        return "Ошибка: невозможно обработать данные котировок"

    main_text = text(
        bold("📊 Курсы валют 📊"), "\n\n",
        bold("💵 USD/RUB"), "\n",
        "• Investing:", " ", code(res['investing']['price']),
        " ", f"\\({res['investing']['change']} руб или {str(res['investing']['percent']).replace('(', '\\(').replace(')', '\\)')}\\)", "\n",
        "• ABCEX \\(USDT\\):", " ", code(res['abcex']), " ",
        ch['abcex'], "\n",
        "• ЦБ РФ:", " ", code(res['centralb']), " ",
        ch['central'], "\n",
        "• XE:", " ", code(res['xe_usd']), " ",
        ch['xe'], "\n\n",
        bold("🇪🇺 EUR/RUB"), "\n",
        "• ЦБ РФ:", " ", code(res['centralb_eur']), "\n",
        "• XE:", " ", code(res['xe_e_r']), "\n\n",
        bold("🇨🇳 CNY/RUB"), "\n",
        "• ЦБ РФ:", " ", code(res['centralb_cny']), "\n\n",
        bold("🌐 Другие пары"), "\n",
        "• XE CNY/USD:", " ", code(res['xe_cny']), "\n",
        "• XE EUR/USD:", " ", code(res['xe_eur'])
    )

    return main_text.replace('+', '\\+').replace('.', ',') if '+' in main_text else main_text.replace('-', '\\-').replace('.', ',')
async def price_correction(imp: dict) -> dict:
    """
    Формирует и рассчитывает соотношение валютной пары USD\\RUB к Investing.com
    :imp: Словарь с данными котировок
    :return: словарь с строками расчета соотношения или None при ошибке
    """
    required_keys = ['investing', 'abcex', 'centralb', 'xe_usd']
    if not all(key in imp for key in required_keys) or 'price' not in imp.get('investing', {}):
        logging.error(f"Отсутствуют необходимые ключи в данных: {imp}")
        return None

    try:
        # Нормализация и преобразование в Decimal
        invest_str = normalize_number_string(imp['investing']['price'])
        abcex_str = normalize_number_string(imp['abcex'])
        central_str = normalize_number_string(imp['centralb'])
        xe_str = normalize_number_string(imp['xe_usd'])

        if any(s is None for s in [invest_str, abcex_str, central_str, xe_str]):
            logging.error(
                f"Некорректные значения: invest={invest_str}, abcex={abcex_str}, central={central_str}, xe={xe_str}, исходные данные: {imp}")
            return None

        invest = Decimal(invest_str)
        abcex = Decimal(abcex_str)
        central = Decimal(central_str)
        xe = Decimal(xe_str)
    except (KeyError, ValueError, InvalidOperation) as e:
        logging.error(f"Ошибка обработки данных: {e}, данные: {imp}")
        return None

    abcex_perc = (abs(invest - abcex) / invest) * 100
    cent_perc = (abs(invest - central) / invest) * 100
    xe_perc = (abs(invest - xe) / invest) * 100

    abcex_perc_str = f'{abcex_perc:.2f}%'
    cent_perc_str = f'{cent_perc:.2f}%'
    abcex_rub_str = f'{abs(invest - abcex):.2f} руб'
    cent_rub_str = f'{abs(invest - central):.2f} руб'
    xe_rub_str = f'{abs(invest - xe):.2f} руб'
    xe_perc_str = f'{xe_perc:.2f}%'

    def pointer(diff): return ['⬆', '➕'] if invest < diff else ['⬇', '➖']

    return {
        "abcex": f"\\({pointer(abcex)[0]} {abcex_perc_str} или {pointer(abcex)[1]}{abcex_rub_str}\\)",
        "central": f"\\({pointer(central)[0]} {cent_perc_str} или {pointer(central)[1]}{cent_rub_str}\\)",
        "xe": f"\\({pointer(xe)[0]} {xe_perc_str} или {pointer(xe)[1]}{xe_rub_str}\\)"
    }


def normalize_number_string(value: str) -> str:
    """Очищает строку с числом, убирая пробелы, неразрывные пробелы и нормализуя разделители."""
    if not value or value.strip() in ('', 'abcex_error'):
        logging.error(f"Пустое или некорректное значение: {value}")
        return None

    # Удаляем пробелы, неразрывные пробелы (\xa0) и заменяем запятую на точку
    cleaned = value.replace('\xa0', '').replace(
        ' ', '').replace(',', '.').strip()

    # Проверяем, является ли строка валидным числом (цифры, точка, возможно минус)
    if not re.match(r'^-?\d*\.?\d+$', cleaned):
        logging.error(
            f"Некорректный формат числа после очистки: {cleaned}, исходное: {value}")
        return None

    return cleaned
