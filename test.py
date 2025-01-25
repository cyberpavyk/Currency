
import asyncio 
import time
from app.other.classes import GetData

async def main():
    pf = GetData()
    for i in range(9):
        match i:
            case 0:
                try:
                    st = time.time()
                    dsf = await pf.central_bank_usd_rub()
                    end = time.time()
                    print(f'результат запроса цб рф - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У цб пизда')
            case 1:
                try:
                    st = time.time()
                    dsf = await pf.investing_usd_rub()
                    end = time.time()
                    print(f'результат запроса investing - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У инвеста пизда')
            case 2:
                try:
                    st = time.time()
                    dsf = await pf.grantex_usd_rub()
                    end = time.time()
                    print(f'результат запроса guruntux - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У gagarantexa пизда')
            case 3:
                try:
                    st = time.time()
                    dsf = await pf.xe_usd_cny()
                    end = time.time()
                    print(f'результат запроса xe_usd_cny  - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У xe пизда')

            case 4:
                try:
                    st = time.time()
                    dsf = await pf.xe_eur_usd()
                    end = time.time()
                    print(f'результат запроса xe_eur_usd - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У xe пизда')
            case 5:
                try:
                    st = time.time()
                    dsf = await pf.xe_usd_rub()
                    end = time.time()
                    print(f'результат запроса xe_rub_usd - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У xe пизда')
            case 6:
                try:
                    st = time.time()
                    dsf = await pf.central_bank_cny_rub()
                    end = time.time()
                    print(f'результат запроса цб рф cny - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У цб пизда')


            case 7:
                try:
                    st = time.time()
                    dsf = await pf.central_bank_eur_rub()
                    end = time.time()
                    print(f'результат запроса цб рф cny - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У цб пизда')
            case 8:
                try:
                    st = time.time()
                    dsf = await pf.central_bank_eur_rub()
                    end = time.time()
                    print(f'результат запроса цб рф cny - {dsf}\n  время - {end-st}\n')
                except TimeoutError:
                    print('У цб пизда')



if __name__ == '__main__':
    
    asyncio.run(main())

