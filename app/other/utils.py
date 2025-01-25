from app.other.classes import GetData
from decimal import Decimal

async def calcuter(platform: str, amount: str ) -> str:
    """

    Рассчитывает сумму в зависимости от платформы и количества.

    :param platform: Платформа для получения курса валют.
    :param amount: Сумма для конвертации в строковом формате.
    :return: Строка с результатом конвертации.
    
    """

    stf = GetData()
    match platform:
        
        # xe 
        case 'xe_rub_usd':
            res = await stf.xe_usd_rub()
            return f'{Decimal(res) * Decimal(amount):.2f} RUB'
        
        case 'xe_eur_usd':
            res = await stf.xe_eur_usd()
            return f'{Decimal(res) * Decimal(amount):.2f} USD'
        
        case 'xe_cny_usd':
            res = await stf.xe_usd_cny()
            return f'{Decimal(res) * Decimal(amount):.2f} CNY'
        
        case 'xe_eur_rub':
            res = await stf.xe_eur_rub()
            return f'{Decimal(res) * Decimal(amount):.2f} RUB'
            
        #CB
        case 'cb_usd_rub':
            res = await stf.central_bank_usd_rub()
            return f'{Decimal(res.replace(",", ".")) * Decimal(amount):.2f} RUB'
        
        case 'cb_cny_rub':
            res = await stf.central_bank_cny_rub()  
            return f'{Decimal(res.replace(",", ".")) * Decimal(amount):.2f} RUB'
        
        case 'cb_eur_rub':
            res = await stf.central_bank_eur_rub()
            return f'{Decimal(res.replace(",", ".")) * Decimal(amount):.2f} RUB'

        #investing
        case 'inv_usd_rub':
            res = await stf.investing_usd_rub()
            return f'{Decimal(res['price'].replace(",", ".")) * Decimal(amount):.2f} RUB'

        #garantex
        case 'gar_usdt_rub':
            res = await stf.grantex_usd_rub()
            return f'{Decimal(res) * Decimal(amount):.2f} RUB'
        
