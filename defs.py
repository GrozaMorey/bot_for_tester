from models import session, User
from aiogram import  types


def get_info(message: types.Message) -> str:
    user = session.query(User).filter_by(username=message.from_user.username).first()

    return f"Оплачена ли подписка: {'Да' if user.pay_in_mouth else 'Нет'}\n" \
           f" Действительна до {str(user.expired)}\n " \
           f"Номер бейджика: {str(user.number_badge)}"

def change_badge(message: types.Message):
    user = session.query(User).filter_by(username=message.from_user.username).first()
    