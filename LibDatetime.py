import datetime

datetime.time
datetime.date.today()
datetime.date.today().year
datetime.date.today().month
datetime.date.today().day
datetime.datetime.utcnow() # get utc time for current time
datetime.datetime.now() # get time for current time
datetime.datetime.utcfromtimestamp() # не работает с отрицательным значение.
datetime.strptime() # «string parse time» - парсинг строки со значением времени. принимает строку формата и возвращает объект datetime.datetime.