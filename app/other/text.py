from app.other.classes import GetData
from decimal import Decimal
async def set_text():
    """

    Формирует текстовое сообщение с котировками валют.

    :return: Строка с котировками валют.

    """

    gd = GetData()
    res: dict = await gd() 
    ch: dict = await price_correction(res)
    
    main_text = (f"Котировки:\n"
                f"Investing USD/RUB💲 - {res["investing"]["price"]} ({res['investing']["change"]} руб или {res["investing"]["percent"][1:-1]})\n"
                f"Garantex USDT/RUB💲 - {res["garantex"]} {ch['garant']}\n"
                f"ЦБ РФ USD/RUB💲 - {res["centralb"]} {ch['central']}\n"
                f"ЦБ РФ CNY/RUB ¥ - {res["centralb_cny"]}\n"
                f"ЦБ РФ EUR/RUB € - {res["centralb_eur"]}\n"
                f"XE USD/RUB💲 - {res["xe_usd"]} {ch['xe']}\n"
                f"XE CHY/USD ¥ - {res["xe_cny"]}\n"
                f"XE EUR/USD € - {res["xe_eur"]}\n"
                f"XE EUR/RUB € - {res["xe_e_r"]}\n"
                
    )
    return main_text



async def price_correction(imp: dict) -> str:
    """
    Формирует и расчитывает соотношение валютной пары USD\RUB
    к Investing.com
    :imp: Словарь с данными котировок
    :return: словарь с строками расчета соотношения
    """
    try:
        invest = Decimal(imp['investing']['price'].replace(',', '.'))
        garant = Decimal(imp['garantex'])
        central = Decimal(imp['centralb'].replace(',', '.'))
        xe = Decimal(imp['xe_usd'])
    except (KeyError, ValueError) as e:
        print(f"Error processing input data: {e}")
        return None
    

    garant_perc = (abs(invest - garant) / invest) * 100
    cent_perc = (abs(invest - central) / invest) * 100
    xe_perc = (abs(invest-xe)/ invest) * 100

    garant_perc_str = f'{garant_perc:.2f}%'
    cent_perc_str = f'{cent_perc:.2f}%'
    gar_rub_str = f'{abs(invest - garant):.2f} руб'
    cent_rub_str = f'{abs(invest - central):.2f} руб'
    xe_rub_str = f'{abs(invest - xe):.2f} руб'
    xe_perc_str = f'{xe_perc:.2f}%'
    
    
    pointer = lambda diff: ['⬆','+'] if invest < diff else ['⬇','-']

    return {
        "garant": f'({pointer(garant)[0]} {garant_perc_str} или {pointer(garant)[1]}{gar_rub_str})',
        "central": f'({pointer(central)[0]} {cent_perc_str} или {pointer(central)[1]}{cent_rub_str})',
        "xe": f'({pointer(xe)[0]} {xe_perc_str} или {pointer(xe)[1]}{xe_rub_str})'

    }