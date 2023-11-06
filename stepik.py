from math import *
a = 1
b = 2
d = 3
c = 4
x = 5
a1 = 1
a2 = 2
y = 3
number2 = fabs((a*x-b)*x+c)*x-d

number3 = ((a + b)/c) + (c/(a*b))

number4 = ((x + y)/a1) * (a2/(x - y))

number5 = (10**4*a)+(3*(1/5)*b)

number6 = (1 + (x/factorial(2)) + (y/factorial(3))) / (1 + (2/(3 + x * y)))


print(number6)

@dp.message_handler(commands=["cancel"], state="*")
async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.reply("Отменино",
                        reply_markup=get_keyboard())
    await state.finish()
    await welcome(message)