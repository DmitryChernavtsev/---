import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import requests
from geo import get_country, get_distance, get_coordinates

TOKEN = '4cfe1ba63a74ee3c7c00195be5a0e830dc6faaaa9e549ac5f56d09debec387f5f84c89aa778fdc1dd8fda'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 189205599)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            request = event.message['text'].lower()

            if request in ('привет', 'здорова', 'здравствуйте', 'хай', 'здрасте', 'салют, '
                                                                                  'hellow', 'hi',
                           'good morning', 'good afternun', 'good evening', 'good night',
                           'приветствую', 'ну привет', 'приветик'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Привет",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in ('пока', 'увидимся', 'прощай', 'до свидания', 'салют'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="До свидания",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in ('как дела', 'как ты', 'как жизнь', 'как жизнь молодая'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Хорошо",
                                                   random_id=random.randint(0, 2 ** 64))
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="А твои?",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in ('кто ты', 'а ты кто', 'это кто'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Я бот",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "чем ты занимаешься?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Думаю",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in (
                    'как Вас зовут?', 'какое твое имя?', 'как тебя по имени?', 'как тебя зовут?',
                    'твое имя?', 'как тебя звать?'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Пока ещё не знаю",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "как ваши дела?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="лучше не бывает",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "как это работает?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Я работаю на сервере и использую "
                                                           "специальный токин ключ и id, чтобы "
                                                           "связываться с вами посредством диалога",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in ('что вы предлагаете?', 'ваше мнение?', 'как ты думаешь?',
                             'твоё мнение?', 'каков твой взгляд?'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Я могу отвечать на ваши вопросы, "
                                                           "предсказывать погоду в городе, "
                                                           "играть в города",
                                                   random_id=random.randint(0, 2 ** 64))
            elif request in ("где вы находитесь?", 'где ты?', 'ты где?', 'где?'):
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Вам туда не попасть",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "вам нравится [известный человек]?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Эрик Давидыч",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "в каком году титаник утонул в атлантическом океане 15 апреля во время своего" \
                 "первого плавания из саутгемптона?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="1912",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "как называется первый фильм «carry on», снятый и выпущенный в 1958 году?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Проводить сержант",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "как называется крупнейшая технологическая компания в южной корее?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Samsung",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой певец выступал в поп-группе Showaddywaddy 1970-х годов?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Дейв Бартрам",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой теперь известный телевизионный шеф начал готовить в возрасте восьми лет в пабе " \
                 "своих родителей «The Cricketers» в Клаверинге, Эссекс?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Джейми Оливер",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой голландский игрок в дартс выиграл чемпионат мира BDO 2012 года в загородном " \
                 "клубе Lakeside, Frimley Green, 15 января?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Кристиан Кист",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой металл был открыт Гансом Кристианом Эрстедом в 1825 году?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="алюминий",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какая столица Португалии?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Лиссабон",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Сколько вдохов делает человеческое тело ежедневно?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="20,000 ежедневно",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Кем был премьер-министр Великобритании с 1841 по 1846 год?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Роберт Пил",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой химический символ для серебра?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Ag",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Кто изобрел Cat's Eyes в 1934 году для " \
                 "повышения безопасности дорожного движения?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Перси Шоу",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какая самая маленькая птица в мире?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Пчела колибри",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Кто играл «Боди» и «Дойл» в «Профессионалах»?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Льюис Коллинз и Мартин Шоу",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какая кукла, Барби, полное имя?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Барбара Миллисент Робертс",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "За что держит рекорд Пол Ханн, который зарегистрировал 118.1 децибела?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Самая громкая отрыжка",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Что на визитной карточке Аль Капоне было указано, чем он занимается?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Продавец подержанной мебели",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какова продолжительность жизни стрекозы?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="24 часа",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком году был выпущен первый грузовик Tonka - 1945, 1947 или 1949?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="1947",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Кто изобрел консервную банку для консервирования в 1810 году?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Питер Дюран",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком году был выпущен Крестный отец?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="1972",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой актер выиграл лучшего актера Оскара за фильмы «Филадельфия» (1993) " \
                 "и «Форрест Гамп» (1994)?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Том Хэнкс",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Сколько самореферентных камей снял Альфред Хичкок в своих фильмах с 1927 по" \
                 " 1976 год - 33, 35 или 37?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="37",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой фильм 1982 года был широко принят поклонниками фильма за то, что он " \
                 "изображал любовь между молодым бездомным мальчиком-пригородом и потерянным, " \
                 "доброжелательным и тоскующим по дому посетителем с другой планеты?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="ET Экстра-земной",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какая актриса сыграла Мэри Поппинс в фильме 1964 года Мэри Поппинс?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Джули Эндрюс",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком классическом фильме 1963 года появился Чарльз Бронсон?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="The Great Escape",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком фильме 1995 года Сандра Баллок сыграла Анжелу Беннетт - Борьба с " \
                 "Эрнестом Хемингуэем, Сеть или 28 дней?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Чистая",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какая новозеландская женщина-режиссер сняла эти фильмы - «В разрезе» (2003 г.), " \
                 "«Водный дневник» (2006 г.) и «Яркая звезда» (2009 г.)?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Джейн Кэмпион",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой актер предоставил голос для персонажа Немо в фильме 2003 года «В поисках Немо»?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Александр Гулд",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Какой заключенный, названный «самым жестоким заключенным в Британии», " \
                 "был героем фильма 2009 года?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Чарльз Бронсон (фильм назывался Бронсон)",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком фильме 2008 года с участием Кристиана Бэйла в главной роли есть такая цитата:" \
                 " «Я верю, что все, что тебя не убивает, просто делает тебя… незнакомцем»?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Темный рыцарь",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Американская актриса, сыгравшая босса преступного мира Токио О-Рен Исии в " \
                 "KillBill Vol I & II.".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Lucy Liu",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком фильме Хью Джекман снимался в роли волшебника-соперника персонажа," \
                 " которого играл Кристиан Бэйл?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Престиж",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Как звали трёх Драконов Дейнерис Таргариен Буре-рождённой?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Дрогон, Визерион, Рейгаль",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "Была ли Серсея правящей королевой?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Да",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "В каком сезоне Санса стала хранительницей Севера?".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="В 8 сезон 6 серии",
                                                   random_id=random.randint(0, 2 ** 64))
            elif "погоду в ".lower() in request:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message=weather(request.split()[-1][:-1]),
                                                   random_id=random.randint(0, 2 ** 64))
            else:
                vk_session.get_api().messages.send(user_id=event.obj.message['from_id'],
                                                   message="Не понял вашего ответа",
                                                   random_id=random.randint(0, 2 ** 64))


def weather(s_city):
    town = "Абакан Азов Александров Алексин Альметьевск Анапа Ангарск Анжеро-Судженск Апатиты Арзамас " \
           "Армавир Арсеньев Артем Архангельск Асбест Астрахань Ачинск Балаково Балахна Балашиха Балашов " \
           "Барнаул Батайск Белгород Белебей Белово Белогорск (Амурская область) Белорецк Белореченск Бердск " \
           "Березники Березовский (Свердловская область) Бийск Биробиджан Благовещенск (Амурская область) Бор" \
           " Борисоглебск Боровичи Братск Брянск Бугульма Буденновск Бузулук Буйнакск Великие Луки Великий " \
           "Новгород Верхняя Пышма Видное Владивосток Владикавказ Владимир Волгоград Волгодонск Волжск " \
           "Волжский Вологда Вольск Воркута Воронеж Воскресенск Воткинск Всеволожск Выборг Выкса Вязьма" \
           " Гатчина Геленджик Георгиевск Глазов Горно-Алтайск Грозный Губкин Гудермес Гуково Гусь-Хрустальный " \
           "Дербент Дзержинск Димитровград Дмитров Долгопрудный Домодедово Донской Дубна Евпатория Егорьевск" \
           " Ейск Екатеринбург Елабуга Елец Ессентуки Железногорск (Красноярский край) Железногорск " \
           " Жигулевск Жуковский Заречный Зеленогорск Зеленодольск Златоуст Иваново Ивантеевка Ижевск " \
           "Избербаш Иркутск Искитим Ишим Ишимбай Йошкар-Ола Казань Калининград Калуга Каменск-Уральский " \
           "Каменск-Шахтинский Камышин Канск Каспийск Кемерово Керчь Кинешма Кириши Киров (Кировская область)" \
           " Кирово-Чепецк Киселевск Кисловодск Клин Клинцы Ковров Когалым Коломна Комсомольск-на-Амуре " \
           "Копейск Королев Кострома Котлас Красногорск Краснодар Краснокаменск Краснокамск Краснотурьинск " \
           "Красноярск Кропоткин Крымск Кстово Кузнецк Кумертау Кунгур Курган Курск Кызыл Лабинск Лениногорск " \
           "Ленинск-Кузнецкий Лесосибирск Липецк Лиски Лобня Лысьва Лыткарино Люберцы Магадан Магнитогорск " \
           "Майкоп Махачкала Междуреченск Мелеуз Миасс Минеральные Воды Минусинск Михайловка Михайловск " \
           "(Ставропольский край) Мичуринск Москва Мурманск Муром Мытищи Набережные Челны Назарово Назрань " \
           "Нальчик Наро-Фоминск Находка Невинномысск Нерюнгри Нефтекамск Нефтеюганск Нижневартовск Нижнекамск " \
           "Нижний Новгород Нижний Тагил Новоалтайск Новокузнецк Новокуйбышевск Новомосковск Новороссийск " \
           "Новосибирск Новотроицк Новоуральск Новочебоксарск Новочеркасск Новошахтинск Новый Уренгой Ногинск" \
           " Норильск Ноябрьск Нягань Обнинск Одинцово Озерск (Челябинская область) Октябрьский Омск Орел " \
           "Оренбург Орехово-Зуево Орск Павлово Павловский Посад Пенза Первоуральск Пермь Петрозаводск " \
           "Петропавловск-Камчатский Подольск Полевской Прокопьевск Прохладный Псков Пушкино Пятигорск " \
           "Раменское Ревда Реутов Ржев Рославль Россошь Ростов-на-Дону Рубцовск Рыбинск Рязань Салават " \
           "Сальск Самара Санкт-Петербург Саранск Сарапул Саратов Саров Свободный Севастополь Северодвинск " \
           "Северск Сергиев Посад Серов Серпухов Сертолово Сибай Симферополь Славянск-на-Кубани Смоленск" \
           " Соликамск Солнечногорск Сосновый Бор Сочи Ставрополь Старый Оскол Стерлитамак Ступино Сургут " \
           "Сызрань Сыктывкар Таганрог Тамбов Тверь Тимашевск Тихвин Тихорецк Тобольск Тольятти Томск Троицк" \
           " Туапсе Туймазы Тула Тюмень Узловая Улан-Удэ Ульяновск Урус-Мартан Усолье-Сибирское Уссурийск " \
           "Усть-Илимск Уфа Ухта Феодосия Фрязино Хабаровск Ханты-Мансийск Хасавюрт Химки Чайковский Чапаевск " \
           "Чебоксары Челябинск Черемхово Череповец Черкесск Черногорск Чехов Чистополь Чита Шадринск Шали " \
           "Шахты Шуя Щекино Щелково Электросталь Элиста Энгельс Южно-Сахалинск Юрга Якутск Ялта Ярославль".split()
    if s_city in ' '.join(town).lower():
        s_city = town[' '.join(town).lower().find(s_city) // len(town)]
    city_id = 0
    appid = "94030d7e142e2356494a0b52b0fdec62"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        pass

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        for i in data['list'][:1]:
            return (i['dt_txt'], '{0:+1.0f}'.format(i['main']['temp']),
                    i['weather'][0]['description'])
    except Exception as e:
        print("Exception (forecast):", e)
        pass


if __name__ == '__main__':
    main()
