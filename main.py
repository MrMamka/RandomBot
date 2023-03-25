import string
import random
import aiogram

bot = aiogram.Bot('')
dp = aiogram.Dispatcher(bot)

password_symbols = string.ascii_letters + string.digits + '-' + '_'
hedgehogs = ['CAACAgIAAxkBAAEG3bBjnez967IQVy3zV34_v7fZwhQs4AAC0hsAAlLVMUlW_UeuUal4QywE',
             'CAACAgIAAxkBAAEG3bJjne0OVl-8EBqdB-gd4qpbCLC_rwACBB0AAkCHMUnEFB3ZQp60XywE',
             'CAACAgIAAxkBAAEG3bRjne9tBoOfmzMLXmTjliBXycTYPwACaR8AAoaQKUkJZ3DejkyuKiwE',
             'CAACAgIAAxkBAAEG3bZjne-ClgjDysQT6IdI2zV221TIfgACGhwAAvBFKUmRDUXeql4TkSwE',
             'CAACAgIAAxkBAAEG3bhjne-YmLyXF7h-R5zebyIKsnaYZQACUx4AAnmjKUlq88aowrJ1rSwE',
             'CAACAgIAAxkBAAEG3bpjne-nORcXtwfztU5jbs7Ia_LWvwACOCAAAhW7MEnYAz3sbHYKvCwE',
             'CAACAgIAAxkBAAEG3bxjne-xW54p5pOpapwd2gLoBSUXRAACIhkAAk0bMUldb50uJcUyICwE',
             'CAACAgIAAxkBAAEG3b5jne_Peu9vObGTwjLWxxYtz1zPPAACxR0AAkYRKUnDmG6zI8XxiywE',
             'CAACAgIAAxkBAAEG3cBjne_aINx9_IE5RQABry3HYAx4M-EAAkMYAAJ00ClJ4Z4l96_hTP4sBA',
             'CAACAgIAAxkBAAEG3cJjne_n0lBwMnbD6XEIaXrz08-cNgACMBoAAoA6MUlSegK79ZpSEywE',
             'CAACAgIAAxkBAAEG3cRjnfAD4hLNdJqoClmy8spgtGRpWAACyRYAAlgiMUlfkLLBeXF_NywE',
             'CAACAgIAAxkBAAEG3cZjnfAQIsw_basxWNKy_waz0yKFFwACmhgAAp2BMUkcz0MZWJxSSSwE',
             'CAACAgIAAxkBAAEG3chjnfAh9WwIi0HcOkoYG_-jHuuu1wAChBgAAvxNMUkp9tvuLH1wmiwE',
             'CAACAgIAAxkBAAEG3cpjnfAzDRrv6vWFKWf7woQi8KWE5AACVhoAAuGsMEkSs0Egol4zpywE',
             'CAACAgIAAxkBAAEG3cxjnfBEwLKlDaRwjfMjhMiovQIaEwAChhYAAk3eMUlFbJcRR4fs4iwE',
             'CAACAgIAAxkBAAEG3c5jnfBXsKuAAndQ1JzTUbGJw75lPAACXB0AAuaSKUkLRj7sOcJQaiwE',
             'CAACAgIAAxkBAAEG3dBjnfBjewPBJtPCVBU_4CntKEv1sQAC0hsAAll_MUnKePRE_wphCywE',
             'CAACAgIAAxkBAAEG3dJjnfB1khL5muCS_SZjm2DFRYHvWwACORcAAnPNMEkfPXP8swRmlSwE',
             'CAACAgIAAxkBAAEG3dRjnfCLepbA3493cCoB_0Yng1xRygACLBsAAslrMEmyE8fzN-wjaCwE',
             'CAACAgIAAxkBAAEG3dZjnfCZUqHY-5BgXQtK2gWsM4aS4QACARcAAkf6MEnK-_4R7_gLbiwE',
             'CAACAgIAAxkBAAEG3dhjnfCltnSEJv67lsssYDzb8lknBwACWBwAAkAtKEm_xCGquuG9AAEsBA',
             'CAACAgIAAxkBAAEG3dpjnfC4-PROTxzIuqzZLHiYJKHh4AACyxgAAumtKUkaKXmRabALlywE',
             'CAACAgIAAxkBAAEG3dxjnfDEYjNf3kKJKMgp2iYv0QH63QAC3RUAAl4LMEkozVBpRs1vUCwE']


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, 'Список команд:\n'
                                            '/roll - принимает 2 числа и возвращает случайное число из диапазона\n'
                                            '/shuffle - принимает последовательность чисел и/или слов и перемешивает '
                                            'их в '
                                            'случайном порядке\n'
                                            '/dice - подкидывает игральную кость\n'
                                            '/password - принимает длину желаемого пароля и генерирует его\n'
                                            '/hedgehog - присылает случайный стикер с ёжиком\n')


@dp.message_handler(commands=['help'])
async def start(message):
    await bot.send_message(message.chat.id, 'Список команд:\n'
                                            '/roll - принимает 2 числа и возвращает случайное число из диапазона\n'
                                            '/shuffle - принимает последовательность чисел и/или слов и перемешивает '
                                            'их в '
                                            'случайном порядке\n'
                                            '/dice - подкидывает игральную кость\n'
                                            '/password - принимает длину желаемого пароля и генерирует его\n'
                                            '/hedgehog - присылает случайный стикер с ёжиком\n')


@dp.message_handler(commands=['roll'])
async def roll(message):
    parsed_message = list(message.text.split())
    if len(parsed_message) != 3:
        await bot.send_message(message.chat.id, 'Команда /roll должна принимать 2 числа')
        return
    try:
        int(parsed_message[1]), int(parsed_message[2])
    except:
        await bot.send_message(message.chat.id, 'Команда /roll должна принимать числа')
        return
    if parsed_message[1] > parsed_message[2]:
        await bot.send_message(message.chat.id, 'Первое число должно быть не больше второго')
        return
    random_int = random.randint(int(parsed_message[1]), int(parsed_message[2]))
    await bot.send_message(message.chat.id, str(random_int))
    return


@dp.message_handler(commands=['shuffle'])
async def shuffle(message):
    parsed_message = list(message.text.split())
    if len(parsed_message) == 1:
        await bot.send_message(message.chat.id, 'Команда /shuffle должна принимать последовательность')
        return
    parsed_message.pop(0)
    random.shuffle(parsed_message)
    await bot.send_message(message.chat.id, ' '.join(parsed_message))
    return


@dp.message_handler(commands=['hedgehog'])
async def hedgehog(message):
    number_of_hedgehog = random.randint(0, len(hedgehogs) - 1)
    await bot.send_sticker(message.chat.id, hedgehogs[number_of_hedgehog])
    return


@dp.message_handler(commands=['dice'])
async def dice(message):
    number_of_img = random.randint(1, 6)
    img = open(str(number_of_img) + '.png', 'rb')
    await bot.send_photo(message.chat.id, img)
    return


@dp.message_handler(commands=['password'])
async def password(message):
    parsed_message = list(message.text.split())
    if len(parsed_message) != 2:
        await bot.send_message(message.chat.id, 'Команда /password должна принимать 1 число')
        return
    try:
        password_len = int(parsed_message[1])
    except:
        await bot.send_message(message.chat.id, 'Команда /password должна принимать число')
        return
    if password_len < 5 or password_len > 100:
        await bot.send_message(message.chat.id, 'Размер пароля должен быть от 5 до 100')
        return
    result = str()
    for _ in range(password_len):
        number_of_symbol = random.randint(0, len(password_symbols) - 1)
        result += password_symbols[number_of_symbol]
    await bot.send_message(message.chat.id, result)
    return


aiogram.executor.start_polling(dp)
