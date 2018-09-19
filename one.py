import requests
import datetime
#Установка адреса бота
url = https://api.telegram.org/bot671290645:AAG23kNaSMHEQ6bYB7j3JHJ23jo-nTQpC8g/
#Поиск последнего сообщения из массива чата с пользователем Telegram.
def lastUpdate(dataEnd):
	res = dataEnd['result']
	totalUpdates = len(res) - 1
	return res[totalUpdates]
#Получение идентификатора чата Telegram
def getChatID(update):
	chatID = update['message']['chat']['id']
	return chatID
#отправка запроса sendMessage боту
def sendResp(chat, value):
	settings = {'chat_id': chat, 'text': value}
	resp = requests.post(url + 'sendMessage', data=settings)
	return resp
#Get-запрос на обновление информации к боту. Результат – строка json. Метод .json позволяет развернуть ее в массив
def getUpdatesJson(request):
	settings = {'timeout': 100, 'offset': None}
	response = requests.get(request + 'getUpdates', data=settings)
	return response.json()
#Главная функция
def main():
	chatID = getChatID(lastUpdate(getUpdatesJson(url)))
	sendResp(chatID, 'Ваше сообщение')
	updateID = lastUpdate(getUpdatesJson(url))['update_id']
	#Бесконечный цикл, который отправляет запросы боту на получение обновлений
	while True:
	#Если обновление есть, отправляем сообщение
	if updateID == lastUpdate(getUpdatesJson(url))['update_id']:
	sendResp(getChatID(lastUpdate(getUpdatesJson(url))), 'проба')
	updateID += 1
	sleep(1)
#Запуск главной функции
if __name__ == '__main__':
	main()