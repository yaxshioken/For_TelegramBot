from aiogram.fsm.state import StatesGroup, State


class Product(StatesGroup):
    category = State()
    product = State()
    amount = State()
class SignUp(StatesGroup):
    name = State()
    phone = State()
    address = State()
    position = State()
    salary = State()
    vacancy = State()


