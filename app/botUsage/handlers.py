from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter

from app.other.text import set_text
from aiogram.fsm.context import FSMContext
from app.states import Calc

import app.botUsage.keyboards as kb
from app.other.utils import calcuter

router = Router()


@router.message(CommandStart())
async def start_msg(message: Message):
    await message.answer(text="Большое приветственное сообщение)",
                         reply_markup=kb.values
                         )
    

@router.callback_query(F.data=='back_to_main')
async def main_menu(callback: CallbackQuery):
    chat_id = callback.from_user.id
    await callback.bot.send_message(text="Выберите пункт⛓️",
                          reply_markup=kb.values,
                          chat_id=chat_id
                          )
    await callback.answer()


@router.callback_query(F.data == 'get_cot')
async def reply_sec(callback: CallbackQuery):
    chat_id = callback.from_user.id

    initial_mess = await callback.bot.send_message(chat_id, text = 'Действие выполняется....')
    await callback.bot.send_chat_action(chat_id, action='typing')
    
    txt = await set_text()
    
    await callback.bot.edit_message_text(
                                        chat_id=chat_id,
                                        message_id=initial_mess.message_id,
                                        text=txt, 
                                        reply_markup=kb.values_end
                                        )

    await callback.answer()



@router.callback_query(F.data=='calc')
async def calculator(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Calc.id)
    chat_id = callback.from_user.id
    nes_msg = await callback.bot.send_message(chat_id,
                                    reply_markup=kb.platforms,
                                    text="Выберите платформу:") 

    await state.update_data(message_id=nes_msg.message_id)
    await callback.answer()


@router.callback_query(F.data=='back_to_plat')
async def calculator(callback: CallbackQuery, state: FSMContext):
    chat_id = callback.from_user.id
    data = await state.get_value('message_id')
    
    await callback.bot.edit_message_text(chat_id=chat_id,
                                        message_id=data, 
                                        reply_markup=kb.platforms,
                                        text="Выберите платформу:") 
    await callback.answer()
    
 
    






"""
xe
"""
@router.callback_query(F.data=='back_to_xe')
@router.callback_query(F.data=='xe')
async def calculator(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value('message_id')
    await state.update_data(platform='')
    chat_id = callback.from_user.id
    
    await callback.bot.edit_message_text(chat_id=chat_id,
                                                   message_id=data,
                                                   reply_markup=kb.xe_couples,
                                                   text="Выберите валютную пару")
    await callback.answer()
    



@router.callback_query(F.data == 'xe_cny_usd')
async def xe_cny(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='xe_cny_usd')
    await callback.bot.edit_message_text(text='Введите количество USD в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_xe
                                         )
    await callback.answer()
    

@router.callback_query(F.data == 'xe_eur_usd')
async def xe_eur(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='xe_eur_usd')
    await callback.bot.edit_message_text(text='Введите количество EUR в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_xe
                                         )
    await callback.answer()
    


@router.callback_query(F.data == 'xe_rub_usd')
async def xe_rub(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='xe_rub_usd')
    await callback.bot.edit_message_text(text='Введите количество USD в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_xe
                                         )
    await callback.answer()
    

@router.callback_query(F.data == 'xe_eur_rub')
async def xe_rub(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='xe_eur_rub')
    await callback.bot.edit_message_text(text='Введите количество EUR в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_xe
                                         )
    await callback.answer()
    



"""
centralb
"""
@router.callback_query(F.data=='back_to_cb')
@router.callback_query(F.data=='cb')
async def calculator(callback: CallbackQuery, state: FSMContext):

    data = await state.get_value('message_id')
    await state.update_data(platform='')
    chat_id = callback.from_user.id
    
    await callback.bot.edit_message_text(chat_id=chat_id,
                                                   message_id=data,
                                                   reply_markup=kb.cb_couples,
                                                   text="Выберите валютную пару")
    await callback.answer()
    


@router.callback_query(F.data == 'cb_usd_rub')
async def cb_usd(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='cb_usd_rub')
    await callback.bot.edit_message_text(text='Введите количество USD в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_cb
                                         )
    await callback.answer()



@router.callback_query(F.data == 'cb_cny_rub')
async def cb_cny(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='xe_cny_usd')
    await callback.bot.edit_message_text(text='Введите количество CNY в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_cb
                                         )
    await callback.answer()



@router.callback_query(F.data == 'cb_eur_rub')
async def cb_eur(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='cb_eur_rub')
    await callback.bot.edit_message_text(text='Введите количество EUR в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_cb
                                         )
    await callback.answer()
    
"""
investing
"""
@router.callback_query(F.data=='back_to_inv')
@router.callback_query(F.data=='investing')
async def calculator(callback: CallbackQuery,state: FSMContext):

    data = await state.get_value('message_id')
    await state.update_data(platform='')
    chat_id = callback.from_user.id
    
    await callback.bot.edit_message_text(chat_id=chat_id,
                                                   message_id=data,
                                                   reply_markup=kb.investing_couples,
                                                   text="Выберите доступную валютную пару")
    await callback.answer()
    


@router.callback_query(F.data == 'inv_usd_rub')
async def xe_cny(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='inv_usd_rub')
    await callback.bot.edit_message_text(text='Введите количество USD в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_inv
                                         )
    await callback.answer()
    

"""
garantex
"""
@router.callback_query(F.data=='back_to_gar')
@router.callback_query(F.data=='garantex')
async def calculator(callback: CallbackQuery,state: FSMContext):

    data = await state.get_value('message_id')
    await state.update_data(platform='')
    chat_id = callback.from_user.id
    
    await callback.bot.edit_message_text(chat_id=chat_id,
                                                   message_id=data,
                                                   reply_markup=kb.garantex_couples,
                                                   text="Выберите доступную валютную пару")
    await callback.answer()
    
@router.callback_query(F.data == 'gar_usdt_rub')
async def xe_cny(callback: CallbackQuery, state: FSMContext):
    data = await state.get_value("message_id") 
    chat_id = callback.from_user.id
    await state.set_state(Calc.input)
    await state.update_data(platform='gar_usdt_rub')
    await callback.bot.edit_message_text(text='Введите количество USDT в формате "nnnn.nn":',
                                         message_id=data,
                                         chat_id=chat_id,
                                         reply_markup=kb.exit_gar
                                         )
    await callback.answer()
    

"""
end
"""
 
@router.message(Calc.input)
async def calulations(message: Message, state: FSMContext):
    amount = message.text 
    chat_id = message.from_user.id

    await message.bot.send_chat_action(chat_id=chat_id, action='typing')

    plat = await state.get_value('platform')
    res = await calcuter(platform=plat, amount=amount)


    await message.answer(text= str(res),
                         reply_markup= kb.back_to_main)

    await state.clear()
