
import asyncio 
import time
from app.other.classes import GetData

async def main():
    pf = GetData()
    requests = [
        (pf.central_bank_usd_rub, 'результат запроса цб рф - {}'),
        (pf.investing_usd_rub, 'результат запроса investing - {}'),
        (pf.grantex_usd_rub, 'результат запроса guruntux - {}'),
        (pf.xe_usd_cny, 'результат запроса xe_usd_cny - {}'),
        (pf.xe_eur_usd, 'результат запроса xe_eur_usd - {}'),
        (pf.xe_usd_rub, 'результат запроса xe_rub_usd - {}'),
        (pf.central_bank_cny_rub, 'результат запроса цб рф cny - {}'),
        (pf.central_bank_eur_rub, 'результат запроса цб рф eur - {}'),
        (pf.central_bank_eur_rub, 'результат запроса цб рф eur - {}'),
    ]

    for i, (request_func, message) in enumerate(requests):
        try:
            st = time.time()
            dsf = await request_func()
            end = time.time()
            print(message.format(dsf))
            print(f'время - {end - st}\n')
        except TimeoutError:
            print(f'Ошибка при выполнении запроса {i + 1}: таймаут.')
        except Exception as e:
            print(f'Ошибка при выполнении запроса {i + 1}: {e}')



if __name__ == '__main__':
    
    asyncio.run(main())

